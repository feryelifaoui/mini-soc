import logging
from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger("router.dashboard")


@router.get("/dashboard/stats", summary="Statistiques globales du SOC")
async def get_dashboard_stats():
    """Retourne les métriques globales du dashboard SOC depuis PostgreSQL."""
    try:
        from database.db import get_dashboard_stats_db
        return get_dashboard_stats_db()
    except Exception as e:
        logger.error(f"Erreur stats dashboard : {e}")
        return {
            "total_incidents": 0,
            "total_tickets": 0,
            "avg_confidence": 0.0,
            "status_distribution": {}
        }


@router.get("/dashboard/incidents", summary="Liste des incidents détectés")
async def get_incidents(limit: int = 50):
    """Retourne l'historique des incidents depuis PostgreSQL."""
    try:
        from database.db import get_all_incidents_db
        return {"incidents": get_all_incidents_db(limit=limit)}
    except Exception as e:
        logger.error(f"Erreur récupération incidents : {e}")
        return {"incidents": [], "error": str(e)}


@router.get("/dashboard/tickets", summary="Liste des tickets ouverts")
async def get_tickets(limit: int = 50):
    """Retourne la liste des tickets depuis PostgreSQL."""
    try:
        from database.db import get_all_tickets_db
        return {"tickets": get_all_tickets_db(limit=limit)}
    except Exception as e:
        logger.error(f"Erreur récupération tickets : {e}")
        return {"tickets": [], "error": str(e)}


from pydantic import BaseModel

class StatusUpdateRequest(BaseModel):
    status: str

@router.put("/dashboard/incidents/{incident_id}/status", summary="Mettre à jour le statut d'un incident")
def update_incident_status(incident_id: int, request: StatusUpdateRequest):
    """Met à jour le statut d'un incident (Nouveau, En cours, Résolu)."""
    try:
        from database.db import update_incident_status_db
        updated = update_incident_status_db(incident_id, request.status)
        if not updated:
            return {"error": "Incident non trouvé", "status": "error"}
        return {"status": "success", "incident": updated}
    except Exception as e:
        logger.error(f"Erreur mise à jour statut incident #{incident_id} : {e}")
        return {"error": str(e), "status": "error"}

