import logging
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()
logger = logging.getLogger("router.agent")


class AgentFlowRequest(BaseModel):
    """Requête d'analyse de flux réseau pour l'Agent IA SOC."""
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


@router.post("/agent/analyze", summary="Analyse complète du flux par l'Agent IA SOC")
def agent_analyze(request: AgentFlowRequest):
    """
    Workflow complet de l'Agent IA SOC :
    - Prédiction ML
    - Enregistrement incident (PostgreSQL)
    - Analyse RAG cybersécurité
    - Génération rapport PDF
    - Envoi email SMTP (feryelifaoui@gmail.com → moncefifaoui0@gmail.com)
    - Création ticket incident (PostgreSQL)
    """
    try:
        from backend.services.agent_service import run_agent_soc_workflow
        features = request.to_model_dict()
        result = run_agent_soc_workflow(features)
        return result
    except Exception as e:
        logger.error(f"Erreur workflow Agent IA SOC : {e}", exc_info=True)
        return {"error": str(e), "status": "error"}
