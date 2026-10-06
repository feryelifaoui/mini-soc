import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Base de données
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/mini_soc")

# Chemins des composants existants
MODEL_PATH = os.getenv("MODEL_PATH", str(BASE_DIR / "modele ml" / "ddos_lgb_model.pkl"))
METADATA_PATH = os.getenv("METADATA_PATH", str(BASE_DIR / "modele ml" / "model_metadata_lgb.json"))
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", str(BASE_DIR / "chatbot-rag" / "faiss_index"))

# Configuration SMTP Mail
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "feryelifaoui@gmail.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "zjxy rqum hzwh hbqt")  # Mot de passe d'application Gmail
DEFAULT_SENDER = os.getenv("DEFAULT_SENDER", "feryelifaoui@gmail.com")
DEFAULT_RECIPIENT = os.getenv("DEFAULT_RECIPIENT", "moncefifaoui0@gmail.com")

# Seuil de confiance
CONFIDENCE_HIGH_THRESHOLD = 0.85
CONFIDENCE_LOW_THRESHOLD = 0.60
