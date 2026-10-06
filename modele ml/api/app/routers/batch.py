"""Router de prédiction batch — POST /api/v1/predict/batch"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.schemas.schemas import NetworkFlowInput, BatchPredictionResponse, BatchPredictionItem, PredictionResponse
from app.core.model import ModelManager
import logging

logger = logging.getLogger("ddos_api.batch")
router = APIRouter()


class BatchPredictionRequest(BaseModel):
    """Corps de la requête pour une prédiction en lot."""
    flows: list[NetworkFlowInput] = Field(
        description="Liste de flux réseau à analyser (maximum 1000 par requête)",
        min_length=1,
        max_length=1000,
    )


@router.post(
    "/predict/batch",
    response_model=BatchPredictionResponse,
    summary="📦 Prédiction DDoS sur plusieurs flux réseau",
    description="""
Analyse un **lot de flux réseau** simultanément et renvoie les prédictions 
pour chaque flux, ainsi qu'un résumé statistique.

### Limites
- Maximum **1000 flux** par requête
- Les flux avec des features manquantes génèrent une entrée `error` dans les résultats

### Résumé de sortie
- `total_flows` : Nombre total de flux analysés
- `ddos_count` : Nombre de flux classifiés comme DDoS
- `benign_count` : Nombre de flux classifiés comme bénins
- `error_count` : Nombre de flux avec erreurs
- `ddos_percentage` : Pourcentage d'attaques DDoS détectées
- `results` : Liste détaillée des prédictions
    """,
    status_code=200,
)
async def predict_batch(request: BatchPredictionRequest) -> BatchPredictionResponse:
    """
    Prédiction en lot sur plusieurs flux réseau simultanément.
    """
    if not ModelManager.is_loaded():
        raise HTTPException(
            status_code=503,
            detail="Le modèle n'est pas encore chargé."
        )

    logger.info(f"Prédiction batch demandée : {len(request.flows)} flux")

    results = []
    ddos_count = 0
    benign_count = 0
    error_count = 0

    for i, flow in enumerate(request.flows):
        features_dict = flow.model_dump(by_alias=True, exclude_none=True)
        try:
            output = ModelManager.predict(features_dict)
            pred_response = PredictionResponse.from_model_output(output)
            item = BatchPredictionItem(
                index=i,
                prediction=pred_response.prediction,
                label=pred_response.label,
                ddos_probability=pred_response.ddos_probability,
                benign_probability=pred_response.benign_probability,
                confidence_score=pred_response.confidence_score,
                confidence_level=pred_response.confidence_level,
                alert=pred_response.alert,
                error=None,
            )
            if pred_response.prediction == 1:
                ddos_count += 1
            else:
                benign_count += 1
        except Exception as e:
            item = BatchPredictionItem(index=i, error=str(e))
            error_count += 1

        results.append(item)

    total = len(request.flows)
    valid_total = ddos_count + benign_count
    ddos_pct = (ddos_count / valid_total * 100) if valid_total > 0 else 0.0

    if ddos_count == 0:
        summary = f"✅ Aucune attaque DDoS détectée sur {total} flux analysés."
    elif ddos_pct >= 50:
        summary = f"🚨 ALERTE CRITIQUE : {ddos_count}/{total} flux ({ddos_pct:.1f}%) identifiés comme DDoS !"
    else:
        summary = f"⚠️ ATTENTION : {ddos_count}/{total} flux ({ddos_pct:.1f}%) suspects détectés."

    logger.info(f"Batch terminé : {ddos_count} DDoS / {benign_count} Bénins / {error_count} Erreurs")

    return BatchPredictionResponse(
        total_flows=total,
        ddos_count=ddos_count,
        benign_count=benign_count,
        error_count=error_count,
        ddos_percentage=round(ddos_pct, 2),
        results=results,
        summary=summary,
    )
