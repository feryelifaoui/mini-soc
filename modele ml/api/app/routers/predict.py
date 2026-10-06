"""Router de prédiction unitaire — POST /api/v1/predict"""

from fastapi import APIRouter, HTTPException
from app.schemas.schemas import NetworkFlowInput, PredictionResponse
from app.core.model import ModelManager
import logging

logger = logging.getLogger("ddos_api.predict")
router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="🔍 Prédiction DDoS sur un flux réseau",
    description="""
Analyse les caractéristiques d'un flux réseau capturé par **CICFlowMeter** 
et détermine s'il s'agit d'un trafic **bénin** ou d'une **attaque DDoS**.

### Traitement
1. Validation des données d'entrée (Pydantic)
2. Alignement sur les features sélectionnées par le modèle
3. Gestion automatique des valeurs NaN/infinies
4. Inférence LightGBM
5. Calcul du score et niveau de confiance

### Sortie
- `prediction` : 0 (Benign) ou 1 (DDoS)
- `label` : "Benign" ou "DDoS"
- `ddos_probability` : Probabilité d'attaque DDoS (0.0 → 1.0)
- `benign_probability` : Probabilité de trafic bénin (0.0 → 1.0)
- `confidence_score` : Score de confiance global
- `confidence_level` : Faible / Moyen / Élevé
- `alert` : Booléen — déclenchement d'alerte SOC
- `alert_message` : Message formaté pour le SOC
    """,
    response_description="Résultat de la prédiction DDoS avec score de confiance",
    status_code=200,
)
async def predict_flow(flow: NetworkFlowInput) -> PredictionResponse:
    """
    Prédit si un flux réseau est bénin ou une attaque DDoS.
    
    Accepte les features CICFlowMeter d'un flux réseau et renvoie la 
    prédiction, la probabilité et le niveau de confiance.
    """
    if not ModelManager.is_loaded():
        raise HTTPException(
            status_code=503,
            detail="Le modèle n'est pas encore chargé. Réessayez dans quelques instants."
        )

    # Conversion du modèle Pydantic en dict avec les alias (noms originaux des features)
    features_dict = flow.model_dump(by_alias=True, exclude_none=True)

    logger.info(f"Prédiction demandée avec {len(features_dict)} features")

    try:
        output = ModelManager.predict(features_dict)
    except ValueError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Erreur de validation des features : {str(e)}"
        )
    except Exception as e:
        logger.error(f"Erreur lors de la prédiction : {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Erreur interne lors de la prédiction : {str(e)}"
        )

    response = PredictionResponse.from_model_output(output)
    logger.info(
        f"Prédiction : {response.label} | "
        f"Probabilité DDoS : {response.ddos_probability:.4f} | "
        f"Confiance : {response.confidence_level}"
    )
    return response
