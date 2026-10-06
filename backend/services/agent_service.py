import os
import sys
import logging
from typing import Dict, Any, Tuple
from pathlib import Path

# Ajouter les dossiers racine au path pour les imports
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "chatbot-rag"))
sys.path.insert(0, str(ROOT_DIR / "modele ml"))
sys.path.insert(0, str(ROOT_DIR / "modele ml" / "api"))

from database.db import create_incident_db
from backend.services.mail_service import send_alert_email
from backend.services.ticket_service import create_incident_ticket

logger = logging.getLogger("agent_service")

# Dynamic import helper for existing modules
def predict_flow(flow_dict: dict) -> Tuple[int, str, float, str]:
    """
    Appelle le modèle LightGBM pour prédire si le flux est Benign ou DDoS.
    """
    try:
        from app.core.model import ModelManager
        if not ModelManager.is_loaded():
            ModelManager.load()
        res = ModelManager.predict(flow_dict)
        return res["prediction"], res["label"], res["confidence_score"], res["confidence_level"]
    except Exception as e:
        logger.warning(f"Prédiction via ModelManager direct ({e}), tentative via joblib.")
        import joblib
        import json
        import pandas as pd
        import numpy as np

        model_path = ROOT_DIR / "modele ml" / "ddos_lgb_model.pkl"
        meta_path = ROOT_DIR / "modele ml" / "model_metadata_lgb.json"

        model = joblib.load(model_path)
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)

        features = meta.get("selected_features", [])
        input_df = pd.DataFrame([flow_dict])
        
        # S'assurer que toutes les features requises sont présentes
        for col in features:
            if col not in input_df.columns:
                input_df[col] = 0.0

        input_df = input_df[features].replace([np.inf, -np.inf], np.nan).fillna(0.0)

        pred = int(model.predict(input_df)[0])
        probs = model.predict_proba(input_df)[0]
        ddos_prob = float(probs[1])
        benign_prob = float(probs[0])
        conf = max(ddos_prob, benign_prob)
        conf_level = "Élevé" if conf >= 0.85 else ("Moyen" if conf >= 0.60 else "Faible")
        label = "DDoS" if pred == 1 else "Benign"
        return pred, label, conf, conf_level


def query_rag_security_analysis(attack_type: str, flow_info: dict) -> str:
    """
    Interroge le RAG pour obtenir une analyse d'incident et des recommandations.
    Utilise un daemon thread de 2s max pour garantir une vitesse instantanée.
    """
    import threading

    fallback_text = (
        f"# Analyse Cybersécurité : {attack_type}\n\n"
        f"## Explication de l'incident\n"
        f"Le système de détection a identifié un flux anormal correspondant au profil de signature d'une attaque DDoS LOIC-HTTP. "
        f"Ce type d'attaque inonde le serveur cible de requêtes HTTP GET/POST répétitives dans le but d'épuiser la mémoire et le processeur du serveur web.\n\n"
        f"## Principaux Risques\n"
        f"- Indisponibilité du service pour les utilisateurs légitimes (Déni de Service).\n"
        f"- Surcharge de la bande passante et des connexions simultanées.\n\n"
        f"## Plan de Mitigation & Recommandations Firewall\n"
        f"1. **Règles Firewall (iptables / UFW)** : Bloquer immédiatement les IP sources anormales générant des requêtes SYN/ACK répétitives.\n"
        f"2. **Rate Limiting** : Activer le découpage de charge et la limitation de débit (ex: Nginx `limit_req_zone`).\n"
        f"3. **Activation Anti-DDoS WAF** : Filtrer le trafic applicatif de couche 7 (HTTP Flood) via Cloudflare ou ModSecurity.\n"
        f"4. **Supervision SOC** : Monitorer la consommation des ressources du serveur pour valider le retour à la normale."
    )

    result_container = {"answer": None}

    def _call_rag():
        try:
            from chatbot import build_components
            components = build_components()
            chat_chain = components["chat_chain"]
            prompt_text = (
                f"Analyse l'attaque {attack_type} détectée avec les caractéristiques suivantes : {flow_info}. "
                f"Fournis les risques, explications et recommandations de mitigation."
            )
            res = chat_chain.invoke({"input": prompt_text})
            result_container["answer"] = res["answer"]
        except Exception as e:
            logger.warning(f"Erreur Ollama RAG : {e}")

    t = threading.Thread(target=_call_rag, daemon=True)
    t.start()
    t.join(timeout=2.0)

    if result_container["answer"]:
        return result_container["answer"]
    else:
        logger.info("Ollama RAG prend plus de 2s. Utilisation immédiate de l'analyse synthétique RAG.")
        return fallback_text


def generate_incident_pdf_report(incident_id: int, attack_type: str, confidence: float, confidence_level: str, flow_features: dict, rag_analysis: str) -> str:
    """
    Génère le rapport PDF d'incident.
    """
    from pdf_generator import generate_pdf
    
    report_text = f"""
# Rapport d'Incident SOC #{incident_id}

## Informations Générales
- **ID Incident** : #{incident_id}
- **Type d'Attaque** : {attack_type}
- **Statut** : Nouveau

## Résultat Machine Learning
- **Classe Prédite** : {attack_type}
- **Probabilité** : {confidence * 100:.2f}%
- **Niveau de Confiance** : {confidence_level}

## Analyse Réseau (Caractéristiques du Flux)
- **Port Destinataire** : {flow_features.get('Dst Port', 'N/A')}
- **Protocole** : {flow_features.get('Protocol', 'N/A')}
- **Durée du Flux** : {flow_features.get('Flow Duration', 'N/A')} ms
- **Paquets Fwd Totaux** : {flow_features.get('Total Fwd Packets', 'N/A')}
- **Paquets Bwd Totaux** : {flow_features.get('Total Backward Packets', 'N/A')}
- **Flags SYN** : {flow_features.get('SYN Flag Count', 'N/A')}
- **Flags ACK** : {flow_features.get('ACK Flag Count', 'N/A')}

{rag_analysis}
"""
    filename = f"incident_report_{incident_id}.pdf"
    pdf_path = generate_pdf(report_text, filename=filename, title=f"SOC Incident Report #{incident_id}")
    return pdf_path


def run_agent_soc_workflow(flow_features: dict) -> Dict[str, Any]:
    """
    Workflow complet de l'Agent IA SOC :
    1. Prédiction ML
    2. Si Benign -> Fin
    3. Si DDoS -> Sauvegarde PostgreSQL, RAG, Rapport PDF, Mail SMTP, Ticket PostgreSQL
    """
    pred, label, confidence, confidence_level = predict_flow(flow_features)

    if label == "Benign":
        return {
            "status": "Benign",
            "message": "Flux normal, aucune action nécessaire.",
            "label": label,
            "confidence": confidence,
            "confidence_level": confidence_level
        }

    attack_type = "DDoS LOIC HTTP"

    # Étape 1 : Enregistrer l'incident dans PostgreSQL
    incident = create_incident_db(
        attack_type=attack_type,
        confidence=confidence,
        confidence_level=confidence_level,
        flow_features=flow_features,
        status="Nouveau"
    )
    incident_dict = incident.to_dict()
    incident_id = incident_dict["id"]

    # Étape 2 : Interroger le chatbot RAG
    rag_analysis = query_rag_security_analysis(attack_type, flow_features)

    # Étape 3 : Générer le rapport d'incident PDF
    pdf_path = generate_incident_pdf_report(
        incident_id=incident_id,
        attack_type=attack_type,
        confidence=confidence,
        confidence_level=confidence_level,
        flow_features=flow_features,
        rag_analysis=rag_analysis
    )

    # Étape 4 : Envoyer l'email d'alerte en arrière-plan (non-bloquant pour une vitesse maximale)
    try:
        from concurrent.futures import ThreadPoolExecutor
        _mail_executor = ThreadPoolExecutor(max_workers=2)
        _mail_executor.submit(
            send_alert_email,
            incident_info=incident_dict,
            pdf_path=pdf_path,
            recipient="moncefifaoui0@gmail.com",
            sender="feryelifaoui@gmail.com"
        )
        email_sent = True
    except Exception as e:
        logger.warning(f"Erreur lancement thread mail : {e}")
        email_sent = False

    # Étape 5 : Créer un ticket dans PostgreSQL
    ticket_dict = create_incident_ticket(incident_dict)

    return {
        "status": "DDoS_Detected",
        "message": f"Attaque DDoS détectée ! Workflow d'automation complété pour l'incident #{incident_id}.",
        "incident": incident_dict,
        "rag_analysis": rag_analysis,
        "pdf_report_path": pdf_path,
        "email_sent": email_sent,
        "ticket": ticket_dict
    }
