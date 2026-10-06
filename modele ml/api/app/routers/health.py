"""Router Health Check — GET /api/v1/health et /api/v1/model/info"""

from fastapi import APIRouter, HTTPException
from app.schemas.schemas import HealthResponse, ModelInfoResponse
from app.core.model import ModelManager
import logging

logger = logging.getLogger("ddos_api.health")
router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="🏥 État de santé de l'API",
    description="""
Vérifie l'état de santé de l'API et du modèle LightGBM chargé.

### Statuts possibles
- `healthy` : API et modèle opérationnels
- `degraded` : API fonctionnelle mais modèle partiellement chargé
- `unhealthy` : Modèle non chargé — prédictions indisponibles

Utilisé pour le monitoring (Prometheus, Wazuh, LoadBalancer health checks).
    """,
    status_code=200,
)
async def health_check() -> HealthResponse:
    """Vérifie l'état de santé de l'API et du modèle."""
    model_loaded = ModelManager.is_loaded()

    if model_loaded:
        try:
            metadata = ModelManager.get_metadata()
            selected_features = ModelManager.get_selected_features()
            metrics = metadata.get("metrics", {})
            status = "healthy"
            message = "✅ API et modèle LightGBM opérationnels."
        except Exception as e:
            status = "degraded"
            selected_features = []
            metrics = {}
            message = f"⚠️ Modèle chargé mais métadonnées inaccessibles : {e}"
    else:
        status = "unhealthy"
        selected_features = []
        metrics = {}
        message = "❌ Modèle non chargé. Prédictions indisponibles."

    return HealthResponse(
        status=status,
        model_loaded=model_loaded,
        model_name="LightGBM DDoS Detector (LOIC-HTTP)",
        selected_features=selected_features,
        metrics=metrics if metrics else None,
        message=message,
    )


@router.get(
    "/model/info",
    response_model=ModelInfoResponse,
    summary="📊 Informations détaillées sur le modèle",
    description="""
Retourne les informations complètes sur le modèle LightGBM chargé :
- Features sélectionnées et exclues
- Hyperparamètres du modèle
- Métriques de performance (Accuracy, F1, ROC-AUC, FAR, etc.)
- Mapping des labels
    """,
    status_code=200,
)
async def model_info() -> ModelInfoResponse:
    """Retourne les métadonnées complètes du modèle chargé."""
    if not ModelManager.is_loaded():
        raise HTTPException(
            status_code=503,
            detail="Le modèle n'est pas chargé. Impossible de récupérer les informations."
        )

    try:
        metadata = ModelManager.get_metadata()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la lecture des métadonnées : {e}")

    return ModelInfoResponse(
        model_type="LightGBM (LGBMClassifier) — Détection DDoS LOIC-HTTP",
        selected_features=metadata.get("selected_features", []),
        excluded_features=metadata.get("excluded_features", []),
        label_map=metadata.get("label_map", {}),
        metrics=metadata.get("metrics", {}),
        model_params=metadata.get("model_params", {}),
    )
