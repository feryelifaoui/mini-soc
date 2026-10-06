"""Schémas Pydantic pour la validation des entrées/sorties de l'API."""

from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, Literal
from enum import Enum


# ═══════════════════════════════════════════════════════════════
# Énumérations
# ═══════════════════════════════════════════════════════════════

class ConfidenceLevel(str, Enum):
    FAIBLE = "Faible"
    MOYEN = "Moyen"
    ELEVE = "Élevé"


class PredictionLabel(str, Enum):
    BENIGN = "Benign"
    DDOS = "DDoS"


# ═══════════════════════════════════════════════════════════════
# Schéma d'entrée — Flux réseau
# ═══════════════════════════════════════════════════════════════

class NetworkFlowInput(BaseModel):
    """
    Caractéristiques d'un flux réseau capturé par CICFlowMeter.
    
    ⚠️ Seules les features sélectionnées par le modèle sont requises.
    Les features de débit (Flow Byts/s, Flow Pkts/s, etc.) sont exclues
    car elles causent un surapprentissage sur les données de laboratoire.
    
    Toutes les valeurs doivent être des nombres réels >= 0.
    Les valeurs infinies ou NaN sont automatiquement remplacées par 0.
    """

    # ── Features de durée et volume ─────────────────────────
    Flow_Duration: Optional[float] = Field(
        None, alias="Flow Duration",
        description="Durée totale du flux réseau (en microsecondes)",
        ge=0, example=1500000.0
    )
    Total_Fwd_Packets: Optional[float] = Field(
        None, alias="Total Fwd Packets",
        description="Nombre total de paquets dans le sens forward",
        ge=0, example=10.0
    )
    Total_Backward_Packets: Optional[float] = Field(
        None, alias="Total Backward Packets",
        description="Nombre total de paquets dans le sens backward",
        ge=0, example=5.0
    )
    Total_Length_of_Fwd_Packets: Optional[float] = Field(
        None, alias="Total Length of Fwd Packets",
        description="Taille totale des paquets forward (en octets)",
        ge=0, example=4500.0
    )
    Total_Length_of_Bwd_Packets: Optional[float] = Field(
        None, alias="Total Length of Bwd Packets",
        description="Taille totale des paquets backward (en octets)",
        ge=0, example=2000.0
    )

    # ── Features de taille des paquets ───────────────────────
    Fwd_Packet_Length_Max: Optional[float] = Field(
        None, alias="Fwd Packet Length Max",
        description="Taille maximale d'un paquet forward (octets)",
        ge=0, example=1514.0
    )
    Fwd_Packet_Length_Min: Optional[float] = Field(
        None, alias="Fwd Packet Length Min",
        description="Taille minimale d'un paquet forward (octets)",
        ge=0, example=40.0
    )
    Fwd_Packet_Length_Mean: Optional[float] = Field(
        None, alias="Fwd Packet Length Mean",
        description="Taille moyenne d'un paquet forward (octets)",
        ge=0, example=450.0
    )
    Fwd_Packet_Length_Std: Optional[float] = Field(
        None, alias="Fwd Packet Length Std",
        description="Écart-type de la taille des paquets forward",
        ge=0, example=200.0
    )
    Bwd_Packet_Length_Max: Optional[float] = Field(
        None, alias="Bwd Packet Length Max",
        description="Taille maximale d'un paquet backward (octets)",
        ge=0, example=1514.0
    )
    Bwd_Packet_Length_Min: Optional[float] = Field(
        None, alias="Bwd Packet Length Min",
        description="Taille minimale d'un paquet backward (octets)",
        ge=0, example=40.0
    )
    Bwd_Packet_Length_Mean: Optional[float] = Field(
        None, alias="Bwd Packet Length Mean",
        description="Taille moyenne d'un paquet backward (octets)",
        ge=0, example=400.0
    )
    Bwd_Packet_Length_Std: Optional[float] = Field(
        None, alias="Bwd Packet Length Std",
        description="Écart-type de la taille des paquets backward",
        ge=0, example=150.0
    )

    # ── Features inter-arrivée ────────────────────────────────
    Flow_IAT_Mean: Optional[float] = Field(
        None, alias="Flow IAT Mean",
        description="Temps inter-arrivée moyen entre paquets (µs)",
        ge=0, example=100000.0
    )
    Flow_IAT_Std: Optional[float] = Field(
        None, alias="Flow IAT Std",
        description="Écart-type du temps inter-arrivée (µs)",
        ge=0, example=50000.0
    )
    Flow_IAT_Max: Optional[float] = Field(
        None, alias="Flow IAT Max",
        description="Temps inter-arrivée maximum (µs)",
        ge=0, example=500000.0
    )
    Flow_IAT_Min: Optional[float] = Field(
        None, alias="Flow IAT Min",
        description="Temps inter-arrivée minimum (µs)",
        ge=0, example=1000.0
    )
    Fwd_IAT_Total: Optional[float] = Field(
        None, alias="Fwd IAT Total",
        description="Temps inter-arrivée total forward (µs)",
        ge=0, example=900000.0
    )
    Fwd_IAT_Mean: Optional[float] = Field(
        None, alias="Fwd IAT Mean",
        description="Temps inter-arrivée moyen forward (µs)",
        ge=0, example=100000.0
    )
    Fwd_IAT_Std: Optional[float] = Field(
        None, alias="Fwd IAT Std",
        description="Écart-type IAT forward (µs)",
        ge=0, example=30000.0
    )
    Fwd_IAT_Max: Optional[float] = Field(
        None, alias="Fwd IAT Max",
        description="IAT maximum forward (µs)",
        ge=0, example=300000.0
    )
    Fwd_IAT_Min: Optional[float] = Field(
        None, alias="Fwd IAT Min",
        description="IAT minimum forward (µs)",
        ge=0, example=5000.0
    )
    Bwd_IAT_Total: Optional[float] = Field(
        None, alias="Bwd IAT Total",
        description="Temps inter-arrivée total backward (µs)",
        ge=0, example=800000.0
    )
    Bwd_IAT_Mean: Optional[float] = Field(
        None, alias="Bwd IAT Mean",
        description="IAT moyen backward (µs)",
        ge=0, example=160000.0
    )
    Bwd_IAT_Std: Optional[float] = Field(
        None, alias="Bwd IAT Std",
        description="Écart-type IAT backward (µs)",
        ge=0, example=40000.0
    )
    Bwd_IAT_Max: Optional[float] = Field(
        None, alias="Bwd IAT Max",
        description="IAT maximum backward (µs)",
        ge=0, example=400000.0
    )
    Bwd_IAT_Min: Optional[float] = Field(
        None, alias="Bwd IAT Min",
        description="IAT minimum backward (µs)",
        ge=0, example=10000.0
    )

    # ── Flags TCP ─────────────────────────────────────────────
    Fwd_PSH_Flags: Optional[float] = Field(
        None, alias="Fwd PSH Flags",
        description="Nombre de flags PSH dans le sens forward",
        ge=0, example=0.0
    )
    Bwd_PSH_Flags: Optional[float] = Field(
        None, alias="Bwd PSH Flags",
        description="Nombre de flags PSH dans le sens backward",
        ge=0, example=0.0
    )
    Fwd_URG_Flags: Optional[float] = Field(
        None, alias="Fwd URG Flags",
        description="Nombre de flags URG dans le sens forward",
        ge=0, example=0.0
    )
    Bwd_URG_Flags: Optional[float] = Field(
        None, alias="Bwd URG Flags",
        description="Nombre de flags URG dans le sens backward",
        ge=0, example=0.0
    )
    FIN_Flag_Count: Optional[float] = Field(
        None, alias="FIN Flag Count",
        description="Nombre de flags FIN dans le flux",
        ge=0, example=1.0
    )
    SYN_Flag_Count: Optional[float] = Field(
        None, alias="SYN Flag Count",
        description="Nombre de flags SYN dans le flux",
        ge=0, example=1.0
    )
    RST_Flag_Count: Optional[float] = Field(
        None, alias="RST Flag Count",
        description="Nombre de flags RST dans le flux",
        ge=0, example=0.0
    )
    PSH_Flag_Count: Optional[float] = Field(
        None, alias="PSH Flag Count",
        description="Nombre total de flags PSH",
        ge=0, example=2.0
    )
    ACK_Flag_Count: Optional[float] = Field(
        None, alias="ACK Flag Count",
        description="Nombre total de flags ACK",
        ge=0, example=8.0
    )
    URG_Flag_Count: Optional[float] = Field(
        None, alias="URG Flag Count",
        description="Nombre total de flags URG",
        ge=0, example=0.0
    )
    CWE_Flag_Count: Optional[float] = Field(
        None, alias="CWE Flag Count",
        description="Nombre de flags CWE",
        ge=0, example=0.0
    )
    ECE_Flag_Count: Optional[float] = Field(
        None, alias="ECE Flag Count",
        description="Nombre de flags ECE",
        ge=0, example=0.0
    )

    # ── Features de fenêtre et header ────────────────────────
    Fwd_Header_Length: Optional[float] = Field(
        None, alias="Fwd Header Length",
        description="Longueur totale des headers forward (octets)",
        ge=0, example=200.0
    )
    Bwd_Header_Length: Optional[float] = Field(
        None, alias="Bwd Header Length",
        description="Longueur totale des headers backward (octets)",
        ge=0, example=100.0
    )
    Fwd_Avg_Bytes_Bulk: Optional[float] = Field(
        None, alias="Fwd Avg Bytes/Bulk",
        description="Octets moyens par bulk forward",
        ge=0, example=0.0
    )
    Fwd_Avg_Packets_Bulk: Optional[float] = Field(
        None, alias="Fwd Avg Packets/Bulk",
        description="Paquets moyens par bulk forward",
        ge=0, example=0.0
    )
    Fwd_Avg_Bulk_Rate: Optional[float] = Field(
        None, alias="Fwd Avg Bulk Rate",
        description="Taux moyen de bulk forward",
        ge=0, example=0.0
    )
    Bwd_Avg_Bytes_Bulk: Optional[float] = Field(
        None, alias="Bwd Avg Bytes/Bulk",
        description="Octets moyens par bulk backward",
        ge=0, example=0.0
    )
    Bwd_Avg_Packets_Bulk: Optional[float] = Field(
        None, alias="Bwd Avg Packets/Bulk",
        description="Paquets moyens par bulk backward",
        ge=0, example=0.0
    )
    Bwd_Avg_Bulk_Rate: Optional[float] = Field(
        None, alias="Bwd Avg Bulk Rate",
        description="Taux moyen de bulk backward",
        ge=0, example=0.0
    )

    # ── Autres features statistiques ─────────────────────────
    Packet_Length_Mean: Optional[float] = Field(
        None, alias="Packet Length Mean",
        description="Taille moyenne de l'ensemble des paquets (octets)",
        ge=0, example=430.0
    )
    Packet_Length_Std: Optional[float] = Field(
        None, alias="Packet Length Std",
        description="Écart-type de la taille des paquets",
        ge=0, example=180.0
    )
    Packet_Length_Variance: Optional[float] = Field(
        None, alias="Packet Length Variance",
        description="Variance de la taille des paquets",
        ge=0, example=32400.0
    )
    Average_Packet_Size: Optional[float] = Field(
        None, alias="Average Packet Size",
        description="Taille moyenne des paquets (octets)",
        ge=0, example=430.0
    )
    Avg_Fwd_Segment_Size: Optional[float] = Field(
        None, alias="Avg Fwd Segment Size",
        description="Taille moyenne des segments forward (octets)",
        ge=0, example=450.0
    )
    Avg_Bwd_Segment_Size: Optional[float] = Field(
        None, alias="Avg Bwd Segment Size",
        description="Taille moyenne des segments backward (octets)",
        ge=0, example=400.0
    )
    Down_Up_Ratio: Optional[float] = Field(
        None, alias="Down/Up Ratio",
        description="Ratio Download/Upload",
        ge=0, example=0.5
    )
    Init_Win_bytes_forward: Optional[float] = Field(
        None, alias="Init_Win_bytes_forward",
        description="Taille initiale de la fenêtre TCP forward (octets)",
        ge=0, example=65535.0
    )
    Init_Win_bytes_backward: Optional[float] = Field(
        None, alias="Init_Win_bytes_backward",
        description="Taille initiale de la fenêtre TCP backward (octets)",
        ge=0, example=65535.0
    )
    act_data_pkt_fwd: Optional[float] = Field(
        None, alias="act_data_pkt_fwd",
        description="Paquets avec données actives forward",
        ge=0, example=8.0
    )
    min_seg_size_forward: Optional[float] = Field(
        None, alias="min_seg_size_forward",
        description="Taille minimale du segment forward (octets)",
        ge=0, example=20.0
    )
    Active_Mean: Optional[float] = Field(
        None, alias="Active Mean",
        description="Durée active moyenne du flux (µs)",
        ge=0, example=0.0
    )
    Active_Std: Optional[float] = Field(
        None, alias="Active Std",
        description="Écart-type de la durée active (µs)",
        ge=0, example=0.0
    )
    Active_Max: Optional[float] = Field(
        None, alias="Active Max",
        description="Durée active maximale (µs)",
        ge=0, example=0.0
    )
    Active_Min: Optional[float] = Field(
        None, alias="Active Min",
        description="Durée active minimale (µs)",
        ge=0, example=0.0
    )
    Idle_Mean: Optional[float] = Field(
        None, alias="Idle Mean",
        description="Durée d'inactivité moyenne (µs)",
        ge=0, example=0.0
    )
    Idle_Std: Optional[float] = Field(
        None, alias="Idle Std",
        description="Écart-type de la durée d'inactivité (µs)",
        ge=0, example=0.0
    )
    Idle_Max: Optional[float] = Field(
        None, alias="Idle Max",
        description="Durée d'inactivité maximale (µs)",
        ge=0, example=0.0
    )
    Idle_Min: Optional[float] = Field(
        None, alias="Idle Min",
        description="Durée d'inactivité minimale (µs)",
        ge=0, example=0.0
    )
    Dst_Port: Optional[float] = Field(
        None, alias="Dst Port",
        description="Port destination du flux réseau",
        ge=0, le=65535, example=80.0
    )
    Protocol: Optional[float] = Field(
        None, alias="Protocol",
        description="Protocole réseau (6=TCP, 17=UDP, etc.)",
        ge=0, example=6.0
    )
    Subflow_Fwd_Packets: Optional[float] = Field(
        None, alias="Subflow Fwd Packets",
        description="Paquets dans le sous-flux forward",
        ge=0, example=10.0
    )
    Subflow_Fwd_Bytes: Optional[float] = Field(
        None, alias="Subflow Fwd Bytes",
        description="Octets dans le sous-flux forward",
        ge=0, example=4500.0
    )
    Subflow_Bwd_Packets: Optional[float] = Field(
        None, alias="Subflow Bwd Packets",
        description="Paquets dans le sous-flux backward",
        ge=0, example=5.0
    )
    Subflow_Bwd_Bytes: Optional[float] = Field(
        None, alias="Subflow Bwd Bytes",
        description="Octets dans le sous-flux backward",
        ge=0, example=2000.0
    )

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Exemple Trafic Bénin (HTTP normal)",
                    "description": "Flux HTTP légitime vers port 80",
                    "value": {
                        "Dst Port": 80.0,
                        "Protocol": 6.0,
                        "Flow Duration": 1500000.0,
                        "Total Fwd Packets": 10.0,
                        "Total Backward Packets": 8.0,
                        "Total Length of Fwd Packets": 4500.0,
                        "Total Length of Bwd Packets": 3200.0,
                        "Fwd Packet Length Max": 1514.0,
                        "Fwd Packet Length Min": 40.0,
                        "Fwd Packet Length Mean": 450.0,
                        "Fwd Packet Length Std": 200.0,
                        "Bwd Packet Length Max": 1514.0,
                        "Bwd Packet Length Min": 40.0,
                        "Bwd Packet Length Mean": 400.0,
                        "Bwd Packet Length Std": 150.0,
                        "Flow IAT Mean": 100000.0,
                        "Flow IAT Std": 50000.0,
                        "Flow IAT Max": 500000.0,
                        "Flow IAT Min": 1000.0,
                        "Fwd IAT Total": 900000.0,
                        "Fwd IAT Mean": 100000.0,
                        "Fwd IAT Std": 30000.0,
                        "Fwd IAT Max": 300000.0,
                        "Fwd IAT Min": 5000.0,
                        "Bwd IAT Total": 700000.0,
                        "Bwd IAT Mean": 100000.0,
                        "Bwd IAT Std": 40000.0,
                        "Bwd IAT Max": 400000.0,
                        "Bwd IAT Min": 10000.0,
                        "Fwd PSH Flags": 0.0,
                        "Bwd PSH Flags": 0.0,
                        "Fwd URG Flags": 0.0,
                        "Bwd URG Flags": 0.0,
                        "Fwd Header Length": 200.0,
                        "Bwd Header Length": 160.0,
                        "FIN Flag Count": 1.0,
                        "SYN Flag Count": 1.0,
                        "RST Flag Count": 0.0,
                        "PSH Flag Count": 2.0,
                        "ACK Flag Count": 8.0,
                        "URG Flag Count": 0.0,
                        "CWE Flag Count": 0.0,
                        "ECE Flag Count": 0.0,
                        "Down/Up Ratio": 0.8,
                        "Average Packet Size": 430.0,
                        "Avg Fwd Segment Size": 450.0,
                        "Avg Bwd Segment Size": 400.0,
                        "Fwd Avg Bytes/Bulk": 0.0,
                        "Fwd Avg Packets/Bulk": 0.0,
                        "Fwd Avg Bulk Rate": 0.0,
                        "Bwd Avg Bytes/Bulk": 0.0,
                        "Bwd Avg Packets/Bulk": 0.0,
                        "Bwd Avg Bulk Rate": 0.0,
                        "Subflow Fwd Packets": 10.0,
                        "Subflow Fwd Bytes": 4500.0,
                        "Subflow Bwd Packets": 8.0,
                        "Subflow Bwd Bytes": 3200.0,
                        "Init_Win_bytes_forward": 65535.0,
                        "Init_Win_bytes_backward": 65535.0,
                        "act_data_pkt_fwd": 8.0,
                        "min_seg_size_forward": 20.0,
                        "Active Mean": 0.0,
                        "Active Std": 0.0,
                        "Active Max": 0.0,
                        "Active Min": 0.0,
                        "Idle Mean": 0.0,
                        "Idle Std": 0.0,
                        "Idle Max": 0.0,
                        "Idle Min": 0.0,
                        "Packet Length Mean": 430.0,
                        "Packet Length Std": 180.0,
                        "Packet Length Variance": 32400.0
                    }
                },
                {
                    "summary": "Exemple Attaque DDoS (LOIC-HTTP)",
                    "description": "Flux typique d'une attaque DDoS LOIC-HTTP — paquets nombreux, courts, IAT très faible",
                    "value": {
                        "Dst Port": 80.0,
                        "Protocol": 6.0,
                        "Flow Duration": 100000.0,
                        "Total Fwd Packets": 5000.0,
                        "Total Backward Packets": 10.0,
                        "Total Length of Fwd Packets": 200000.0,
                        "Total Length of Bwd Packets": 1400.0,
                        "Fwd Packet Length Max": 1514.0,
                        "Fwd Packet Length Min": 40.0,
                        "Fwd Packet Length Mean": 40.0,
                        "Fwd Packet Length Std": 1.0,
                        "Bwd Packet Length Max": 140.0,
                        "Bwd Packet Length Min": 140.0,
                        "Bwd Packet Length Mean": 140.0,
                        "Bwd Packet Length Std": 0.0,
                        "Flow IAT Mean": 20.0,
                        "Flow IAT Std": 5.0,
                        "Flow IAT Max": 100.0,
                        "Flow IAT Min": 1.0,
                        "Fwd IAT Total": 99000.0,
                        "Fwd IAT Mean": 20.0,
                        "Fwd IAT Std": 5.0,
                        "Fwd IAT Max": 100.0,
                        "Fwd IAT Min": 1.0,
                        "Bwd IAT Total": 500.0,
                        "Bwd IAT Mean": 50.0,
                        "Bwd IAT Std": 10.0,
                        "Bwd IAT Max": 100.0,
                        "Bwd IAT Min": 10.0,
                        "Fwd PSH Flags": 0.0,
                        "Bwd PSH Flags": 0.0,
                        "Fwd URG Flags": 0.0,
                        "Bwd URG Flags": 0.0,
                        "Fwd Header Length": 100000.0,
                        "Bwd Header Length": 200.0,
                        "FIN Flag Count": 0.0,
                        "SYN Flag Count": 5000.0,
                        "RST Flag Count": 0.0,
                        "PSH Flag Count": 0.0,
                        "ACK Flag Count": 5000.0,
                        "URG Flag Count": 0.0,
                        "CWE Flag Count": 0.0,
                        "ECE Flag Count": 0.0,
                        "Down/Up Ratio": 0.002,
                        "Average Packet Size": 40.1,
                        "Avg Fwd Segment Size": 40.0,
                        "Avg Bwd Segment Size": 140.0,
                        "Fwd Avg Bytes/Bulk": 0.0,
                        "Fwd Avg Packets/Bulk": 0.0,
                        "Fwd Avg Bulk Rate": 0.0,
                        "Bwd Avg Bytes/Bulk": 0.0,
                        "Bwd Avg Packets/Bulk": 0.0,
                        "Bwd Avg Bulk Rate": 0.0,
                        "Subflow Fwd Packets": 5000.0,
                        "Subflow Fwd Bytes": 200000.0,
                        "Subflow Bwd Packets": 10.0,
                        "Subflow Bwd Bytes": 1400.0,
                        "Init_Win_bytes_forward": 65535.0,
                        "Init_Win_bytes_backward": 65535.0,
                        "act_data_pkt_fwd": 0.0,
                        "min_seg_size_forward": 20.0,
                        "Active Mean": 0.0,
                        "Active Std": 0.0,
                        "Active Max": 0.0,
                        "Active Min": 0.0,
                        "Idle Mean": 0.0,
                        "Idle Std": 0.0,
                        "Idle Max": 0.0,
                        "Idle Min": 0.0,
                        "Packet Length Mean": 40.1,
                        "Packet Length Std": 10.0,
                        "Packet Length Variance": 100.0
                    }
                }
            ]
        }
    }


# ═══════════════════════════════════════════════════════════════
# Schémas de sortie — Réponses
# ═══════════════════════════════════════════════════════════════

class PredictionResponse(BaseModel):
    """Réponse d'une prédiction unitaire."""

    prediction: int = Field(
        description="Classe prédite : 0 = Benign, 1 = DDoS",
        example=1
    )
    label: PredictionLabel = Field(
        description="Label textuel de la prédiction",
        example="DDoS"
    )
    ddos_probability: float = Field(
        description="Probabilité que le flux soit une attaque DDoS (0.0 → 1.0)",
        ge=0.0, le=1.0, example=0.9874
    )
    benign_probability: float = Field(
        description="Probabilité que le flux soit bénin (0.0 → 1.0)",
        ge=0.0, le=1.0, example=0.0126
    )
    confidence_score: float = Field(
        description="Score de confiance de la prédiction (max des deux probabilités)",
        ge=0.0, le=1.0, example=0.9874
    )
    confidence_level: ConfidenceLevel = Field(
        description="Niveau de confiance qualitatif : Faible / Moyen / Élevé",
        example="Élevé"
    )
    alert: bool = Field(
        description="True si une alerte SOC doit être déclenchée",
        example=True
    )
    alert_message: str = Field(
        description="Message d'alerte pour le SOC",
        example="🚨 ALERTE : Attaque DDoS détectée avec une confiance Élevé (98.74%)"
    )

    @classmethod
    def from_model_output(cls, output: dict) -> "PredictionResponse":
        is_ddos = output["prediction"] == 1
        confidence_pct = output["confidence_score"] * 100

        if is_ddos:
            alert_message = (
                f"🚨 ALERTE : Attaque DDoS détectée avec une confiance "
                f"{output['confidence_level']} ({confidence_pct:.2f}%)"
            )
        else:
            alert_message = (
                f"✅ Trafic Bénin — Aucune menace détectée "
                f"(confiance {output['confidence_level']}: {confidence_pct:.2f}%)"
            )

        return cls(
            prediction=output["prediction"],
            label=output["label"],
            ddos_probability=output["ddos_probability"],
            benign_probability=output["benign_probability"],
            confidence_score=output["confidence_score"],
            confidence_level=output["confidence_level"],
            alert=is_ddos,
            alert_message=alert_message,
        )


class BatchPredictionItem(BaseModel):
    """Résultat pour un flux dans une prédiction batch."""
    index: int
    prediction: Optional[int] = None
    label: Optional[PredictionLabel] = None
    ddos_probability: Optional[float] = None
    benign_probability: Optional[float] = None
    confidence_score: Optional[float] = None
    confidence_level: Optional[ConfidenceLevel] = None
    alert: Optional[bool] = None
    error: Optional[str] = None


class BatchPredictionResponse(BaseModel):
    """Réponse d'une prédiction batch."""
    total_flows: int
    ddos_count: int
    benign_count: int
    error_count: int
    ddos_percentage: float
    results: list[BatchPredictionItem]
    summary: str


class HealthResponse(BaseModel):
    """Réponse du health check."""
    status: Literal["healthy", "degraded", "unhealthy"]
    model_loaded: bool
    model_name: str
    selected_features: list[str]
    metrics: Optional[dict] = None
    message: str


class ModelInfoResponse(BaseModel):
    """Informations détaillées sur le modèle chargé."""
    model_type: str
    selected_features: list[str]
    excluded_features: list[str]
    label_map: dict
    metrics: dict
    model_params: dict
