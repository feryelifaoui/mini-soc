"""
╔══════════════════════════════════════════════════════════╗
║         Mini SOC Intelligent — FastAPI Backend           ║
║         Auteur : Équipe Cybersécurité ESPRIT              ║
║         Version : 2.0.0                                  ║
╚══════════════════════════════════════════════════════════╝
"""

import sys
import logging
from pathlib import Path
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Ajouter les dossiers racine au PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "chatbot-rag"))
sys.path.insert(0, str(ROOT_DIR / "modele ml" / "api"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-8s │ %(name)s │ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("mini_soc_backend")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(" Démarrage du Mini SOC Backend...")

    # Initialisation de la base de données
    try:
        from database.db import init_db
        init_db()
        logger.info(" Base de données initialisée avec succès.")
    except Exception as e:
        logger.warning(f" Avertissement DB : {e}")

    # Pré-chargement du modèle ML (optionnel / non-bloquant)
    try:
        import asyncio
        from backend.services.agent_service import predict_flow
        asyncio.get_event_loop().run_in_executor(
            None,
            predict_flow,
            {
                "Dst Port": 80, "Protocol": 6, "Flow Duration": 1000,
                "Total Fwd Packets": 10, "Total Backward Packets": 5,
                "Flow IAT Mean": 100, "Fwd Packet Length Mean": 512,
                "Bwd Packet Length Mean": 256, "SYN Flag Count": 1, "ACK Flag Count": 1
            }
        )
        logger.info(" Pré-chargement ML initié.")
    except Exception as e:
        logger.warning(f" Modèle ML non pré-chargé : {e}")

    yield
    logger.info(" Arrêt du Mini SOC Backend.")


app = FastAPI(
    title=" Mini SOC Intelligent — API Backend",
    description="""
## Plateforme Mini SOC Intelligent

Backend central orchestrant les composants du **Mini Security Operations Center (SOC)** :

-  **Agent IA SOC** : Workflow autonome de détection et réponse aux attaques DDoS
-  **Dashboard SOC** : Métriques, historique des incidents et tickets (PostgreSQL)
-  **Chatbot RAG** : Assistant cybersécurité LangChain + FAISS + Ollama
-  **Détection ML** : Modèle LightGBM entraîné sur CICFlowMeter/CIC-CSE-IDS2018

### Workflow Agent IA SOC (DDoS Détecté) :
1. Prédiction ML du flux réseau
2. Enregistrement de l'incident dans PostgreSQL
3. Analyse RAG (recommandations de mitigation)
4. Génération du rapport PDF
5. Envoi email SMTP (`feryelifaoui@gmail.com` → `moncefifaoui0@gmail.com`)
6. Création d'un ticket dans PostgreSQL
    """,
    version="2.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import et inclusion des routers
from backend.routers import predict, rag, dashboard, agent

app.include_router(predict.router, prefix="/api/v1", tags=[" Prédiction ML"])
app.include_router(rag.router, prefix="/api/v1", tags=[" Chatbot RAG"])
app.include_router(dashboard.router, prefix="/api/v1", tags=[" Dashboard SOC"])
app.include_router(agent.router, prefix="/api/v1", tags=[" Agent IA SOC"])


@app.get("/", tags=[" Accueil"])
async def root():
    return {
        "service": "Mini SOC Intelligent — Backend",
        "version": "2.0.0",
        "status": "operational",
        "docs": "/docs",
        "endpoints": {
            "predict": "/api/v1/predict",
            "rag_chat": "/api/v1/rag/chat",
            "agent_analyze": "/api/v1/agent/analyze",
            "dashboard_stats": "/api/v1/dashboard/stats",
            "incidents": "/api/v1/dashboard/incidents",
            "tickets": "/api/v1/dashboard/tickets",
        }
    }


@app.get("/health", tags=[" Health"])
async def health():
    return {"status": "healthy", "service": "mini-soc-backend"}
