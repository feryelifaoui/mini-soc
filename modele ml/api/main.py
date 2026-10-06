"""
╔══════════════════════════════════════════════════════════════════╗
║     API de Détection DDoS — Mini-SOC | LightGBM + FastAPI       ║
║     Auteur  : Équipe SOC / Stage Cybersécurité                   ║
║     Version : 1.0.0                                              ║
╚══════════════════════════════════════════════════════════════════╝
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import time
import logging

from app.routers import predict, health, batch
from app.core.model import ModelManager
from app.core.config import settings

# ─────────────────────────────────────────────
# Configuration du logger
# ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-8s │ %(name)s │ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("ddos_api")


# ─────────────────────────────────────────────
# Lifecycle : chargement du modèle au démarrage
# ─────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Charge le modèle LightGBM et les métadonnées au démarrage."""
    logger.info("🚀 Démarrage de l'API DDoS Detection...")
    try:
        ModelManager.load()
        logger.info("✅ Modèle LightGBM chargé avec succès.")
    except Exception as e:
        logger.error(f"❌ Échec du chargement du modèle : {e}")
        raise RuntimeError(f"Impossible de charger le modèle : {e}") from e
    yield
    logger.info("🛑 Arrêt de l'API DDoS Detection.")


# ─────────────────────────────────────────────
# Création de l'application FastAPI
# ─────────────────────────────────────────────
app = FastAPI(
    title="🛡️ DDoS Detection API",
    description="""
## API de Détection d'Attaques DDoS — Mini-SOC

Cette API expose un modèle **LightGBM** entraîné sur des captures réseau CICFlowMeter 
pour détecter en temps réel les attaques DDoS de type **LOIC-HTTP**.

### Fonctionnalités
- 🔍 **Prédiction unitaire** : Analyse d'un flux réseau unique
- 📦 **Prédiction en batch** : Analyse de plusieurs flux simultanément
- 📊 **Probabilité** : Score de confiance de la prédiction (0.0 → 1.0)
- 🎯 **Niveau de confiance** : Classification qualitative (Faible / Moyen / Élevé)
- 🏥 **Health Check** : Monitoring de l'état du modèle

### Labels de sortie
| Code | Label   | Signification                            |
|------|---------|------------------------------------------|
| `0`  | Benign  | Trafic légitime, aucune menace détectée  |
| `1`  | DDoS    | Attaque DDoS détectée — Alerte SOC       |

### Fonctionnement
Le modèle analyse les caractéristiques statistiques d'un flux réseau 
(durée, taille des paquets, flags TCP, etc.) et prédit s'il s'agit d'un 
trafic bénin ou d'une attaque DDoS.
    """,
    version="1.0.0",
    contact={
        "name": "Équipe Mini-SOC",
        "email": "soc@lenstate.local",
    },
    license_info={
        "name": "MIT",
    },
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# ─────────────────────────────────────────────
# Middleware CORS
# ─────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─────────────────────────────────────────────
# Middleware de logging des requêtes
# ─────────────────────────────────────────────
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = (time.time() - start_time) * 1000
    logger.info(
        f"{request.method} {request.url.path} → {response.status_code} [{duration:.1f}ms]"
    )
    return response


# ─────────────────────────────────────────────
# Gestionnaire d'erreurs global
# ─────────────────────────────────────────────
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "path": str(request.url.path),
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Erreur inattendue sur {request.url.path} : {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Erreur interne du serveur",
            "detail": str(exc),
            "path": str(request.url.path),
        },
    )


# ─────────────────────────────────────────────
# Inclusion des routers
# ─────────────────────────────────────────────
app.include_router(health.router, prefix="/api/v1", tags=["🏥 Health & Status"])
app.include_router(predict.router, prefix="/api/v1", tags=["🔍 Prédiction Unitaire"])
app.include_router(batch.router, prefix="/api/v1", tags=["📦 Prédiction Batch"])


# ─────────────────────────────────────────────
# Route racine
# ─────────────────────────────────────────────
@app.get(
    "/",
    summary="Page d'accueil",
    description="Informations générales sur l'API de détection DDoS.",
    tags=["🏠 Accueil"],
)
async def root():
    return {
        "service": "DDoS Detection API",
        "version": "1.0.0",
        "status": "operational",
        "model": "LightGBM (LOIC-HTTP DDoS Detector)",
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc",
            "openapi": "/openapi.json",
        },
        "endpoints": {
            "health": "/api/v1/health",
            "predict": "/api/v1/predict",
            "predict_batch": "/api/v1/predict/batch",
            "model_info": "/api/v1/model/info",
        },
    }
