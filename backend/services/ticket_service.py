import logging
from typing import Dict, Any

from database.db import create_ticket_db

logger = logging.getLogger("ticket_service")

def create_incident_ticket(incident_info: Dict[str, Any]) -> Dict[str, Any]:
    """
    Crée automatiquement un ticket d'incident dans la base de données PostgreSQL.
    """
    incident_id = incident_info.get("id")
    attack_type = incident_info.get("attack_type", "DDoS")
    confidence = incident_info.get("confidence", 0.0)
    
    title = f"Ticket #{incident_id} - Analyse & Mitigation Attaque {attack_type}"
    description = (
        f"Incident #{incident_id} généré automatiquement suite à la détection "
        f"d'un trafic malveillant de type {attack_type} avec un niveau de confiance "
        f"de {confidence * 100:.4f}%.\n"
        f"Action requise : Appliquer les règles firewall recommandées et vérifier les logs."
    )
    
    ticket = create_ticket_db(
        incident_id=incident_id,
        title=title,
        description=description,
        priority="Haute",
        status="Ouvert",
        assigned_to="SOC Analyst"
    )
    
    logger.info(f" Ticket #{ticket.id} créé automatiquement pour l'incident #{incident_id}")
    return ticket.to_dict()
