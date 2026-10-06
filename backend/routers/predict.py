import sys
import logging
from pathlib import Path
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()
logger = logging.getLogger("router.predict")


class FlowFeatures(BaseModel):
    """Modèle de données pour les features d'un flux réseau CICFlowMeter."""
    dst_port: float = 0.0
    protocol: float = 0.0
    flow_duration: float = 0.0
    total_fwd_packets: float = 0.0
    total_backward_packets: float = 0.0
    flow_iat_mean: float = 0.0
    fwd_packet_length_mean: float = 0.0
    bwd_packet_length_mean: float = 0.0
    syn_flag_count: float = 0.0
    ack_flag_count: float = 0.0

    def to_model_dict(self) -> Dict[str, Any]:
        return {
            "Dst Port": self.dst_port,
            "Protocol": self.protocol,
            "Flow Duration": self.flow_duration,
            "Total Fwd Packets": self.total_fwd_packets,
            "Total Backward Packets": self.total_backward_packets,
            "Flow IAT Mean": self.flow_iat_mean,
            "Fwd Packet Length Mean": self.fwd_packet_length_mean,
            "Bwd Packet Length Mean": self.bwd_packet_length_mean,
            "SYN Flag Count": self.syn_flag_count,
            "ACK Flag Count": self.ack_flag_count,
        }


@router.post("/predict", summary="Prédiction ML d'un flux réseau")
def predict_single_flow(features: FlowFeatures):
    """
    Effectue une prédiction DDoS sur un flux réseau unique.
    Retourne: label (Benign/DDoS), probabilité et niveau de confiance.
    """
    try:
        from backend.services.agent_service import predict_flow
        pred, label, confidence, confidence_level = predict_flow(features.to_model_dict())
        return {
            "prediction": pred,
            "label": label,
            "confidence": confidence,
            "confidence_level": confidence_level,
            "message": "Flux normal." if label == "Benign" else "⚠️ Attaque DDoS détectée !"
        }
    except Exception as e:
        logger.error(f"Erreur prédiction : {e}")
        return {"error": str(e)}, 500
