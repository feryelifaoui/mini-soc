"""Configuration globale de l'API."""
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  # racine du projet (stage/)


class Settings(BaseSettings):
    # ── Modèle ──────────────────────────────────────────────
    MODEL_PATH: str = str(BASE_DIR / "modele ml" / "ddos_lgb_model.pkl")
    METADATA_PATH: str = str(BASE_DIR / "modele ml" / "model_metadata_lgb.json")

    # ── API ─────────────────────────────────────────────────
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_RELOAD: bool = True

    # ── Seuils de confiance ──────────────────────────────────
    CONFIDENCE_LOW_THRESHOLD: float = 0.60
    CONFIDENCE_HIGH_THRESHOLD: float = 0.85

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
