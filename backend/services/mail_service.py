import os
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from typing import Optional

from backend.config import (
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_USERNAME,
    SMTP_PASSWORD,
    DEFAULT_SENDER,
    DEFAULT_RECIPIENT,
)

logger = logging.getLogger("mail_service")

def send_alert_email(
    incident_info: dict,
    pdf_path: Optional[str] = None,
    recipient: str = DEFAULT_RECIPIENT,
    sender: str = DEFAULT_SENDER
) -> bool:
    """
    Envoie un email d'alerte SOC avec le rapport PDF joint.
    Expéditeur : feryelifaoui@gmail.com
    Destinataire : moncefifaoui0@gmail.com
    """
    subject = f"ALERTE SOC - Attaque DDoS Détectée (Incident #{incident_info.get('id', 'N/A')})"
    
    body = f"""
======================================================================
                  SECURITY OPERATIONS CENTER - ALERTE INCIDENT
======================================================================

Une attaque réseau à haut risque a été automatiquement détectée par le Mini SOC Intelligent.

INFORMATIONS SUR L'INCIDENT :
----------------------------------------------------------------------
- ID Incident       : #{incident_info.get('id', 'N/A')}
- Type d'Attaque    : {incident_info.get('attack_type', 'DDoS LOIC HTTP')}
- Niveau de Confiance: {incident_info.get('confidence_level', 'Élevé')} ({incident_info.get('confidence', 0.0) * 100:.1f}%)
- Statut           : {incident_info.get('status', 'Nouveau')}
- Date              : {incident_info.get('timestamp', 'À l\'instant')}

RECOMMANDATION SOC :
----------------------------------------------------------------------
Veuillez consulter le rapport d'incident complet ci-joint pour les étapes 
de mitigation et de reconfiguration du pare-feu.

----------------------------------------------------------------------
Expéditeur: {sender}
Destinataire Responsable Attaques: {recipient}
    """

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # Pièce jointe PDF s'il existe
    if pdf_path and os.path.exists(pdf_path):
        try:
            with open(pdf_path, "rb") as f:
                attach = MIMEApplication(f.read(), _subtype="pdf")
                attach.add_header(
                    'Content-Disposition', 
                    'attachment', 
                    filename=os.path.basename(pdf_path)
                )
                msg.attach(attach)
        except Exception as e:
            logger.error(f" Erreur lors de l'attachement du PDF : {e}")

    # Tentative d'envoi SMTP
    if not SMTP_PASSWORD:
        logger.warning(
            f" SMTP_PASSWORD non configuré. Mode simulation d'envoi activé :\n"
            f"   De : {sender}\n"
            f"   À : {recipient}\n"
            f"   Sujet : {subject}\n"
            f"   Fichier PDF attaché : {pdf_path}"
        )
        return True

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        logger.info(f" Email d'alerte envoyé avec succès à {recipient}")
        return True
    except Exception as e:
        logger.error(f" Échec de l'envoi SMTP ({e}). Fallback simulation réussi.")
        return False
