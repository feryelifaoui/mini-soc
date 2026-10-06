"""
Gestionnaire du modèle LightGBM.
Charge le modèle et ses métadonnées une seule fois (singleton).
"""

import joblib
import json
import logging
import numpy as np
import pandas as pd
from typing import Optional
from pathlib import Path

from app.core.config import settings

logger = logging.getLogger("ddos_api.model")


class ModelManager:
    """Singleton pour le chargement et l'utilisation du modèle LightGBM."""

    _model = None
    _metadata: Optional[dict] = None
    _selected_features: Optional[list] = None

    @classmethod
    def load(cls) -> None:
        """Charge le modèle LightGBM et les métadonnées depuis le disque."""
        model_path = Path(settings.MODEL_PATH)
        metadata_path = Path(settings.METADATA_PATH)

        # ── Vérification des fichiers ────────────────────────
        if not model_path.exists():
            raise FileNotFoundError(
                f"Fichier modèle introuvable : {model_path}\n"
                "Exécutez d'abord le notebook 'ddos_lightgbm.ipynb' pour entraîner le modèle."
            )
        if not metadata_path.exists():
            raise FileNotFoundError(
                f"Fichier de métadonnées introuvable : {metadata_path}\n"
                "Exécutez d'abord le notebook 'ddos_lightgbm.ipynb'."
            )

        # ── Chargement ───────────────────────────────────────
        logger.info(f"Chargement du modèle depuis : {model_path}")
        cls._model = joblib.load(model_path)

        logger.info(f"Chargement des métadonnées depuis : {metadata_path}")
        with open(metadata_path, "r", encoding="utf-8") as f:
            cls._metadata = json.load(f)

        cls._selected_features = cls._metadata.get("selected_features", [])
        logger.info(f"Features sélectionnées : {cls._selected_features}")

    @classmethod
    def is_loaded(cls) -> bool:
        return cls._model is not None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            raise RuntimeError("Le modèle n'est pas chargé. Appelez ModelManager.load() d'abord.")
        return cls._model

    @classmethod
    def get_metadata(cls) -> dict:
        if cls._metadata is None:
            raise RuntimeError("Les métadonnées ne sont pas chargées.")
        return cls._metadata

    @classmethod
    def get_selected_features(cls) -> list:
        if cls._selected_features is None:
            raise RuntimeError("Les features ne sont pas chargées.")
        return cls._selected_features

    @classmethod
    def predict(cls, features_dict: dict) -> dict:
        """
        Effectue une prédiction à partir d'un dictionnaire de features.

        Args:
            features_dict: Dictionnaire {feature_name: value}

        Returns:
            dict avec prediction, probability, confidence_level, label
        """
        model = cls.get_model()
        selected_features = cls.get_selected_features()

        # ── Construction du DataFrame d'entrée ───────────────
        try:
            input_df = pd.DataFrame([features_dict])
        except Exception as e:
            raise ValueError(f"Erreur lors de la construction du DataFrame : {e}")

        # ── Vérification et alignement des features ──────────
        missing_features = [f for f in selected_features if f not in input_df.columns]
        if missing_features:
            raise ValueError(
                f"Features manquantes : {missing_features}. "
                f"Features attendues : {selected_features}"
            )

        # Sélection et ordre correct des features
        input_df = input_df[selected_features]

        # ── Gestion des valeurs infinies / NaN ───────────────
        input_df = input_df.replace([np.inf, -np.inf], np.nan)
        for col in input_df.columns:
            if input_df[col].isnull().any():
                input_df[col] = input_df[col].fillna(0.0)

        # ── Prédiction ───────────────────────────────────────
        prediction = int(model.predict(input_df)[0])
        probabilities = model.predict_proba(input_df)[0]
        ddos_probability = float(probabilities[1])
        benign_probability = float(probabilities[0])

        # ── Niveau de confiance ───────────────────────────────
        confidence_score = max(ddos_probability, benign_probability)
        confidence_level = cls._compute_confidence_level(confidence_score)

        label = "DDoS" if prediction == 1 else "Benign"

        return {
            "prediction": prediction,
            "label": label,
            "ddos_probability": round(ddos_probability, 6),
            "benign_probability": round(benign_probability, 6),
            "confidence_score": round(confidence_score, 6),
            "confidence_level": confidence_level,
        }

    @classmethod
    def predict_batch(cls, features_list: list[dict]) -> list[dict]:
        """Prédiction en lot sur une liste de flux réseau."""
        model = cls.get_model()
        selected_features = cls.get_selected_features()

        results = []
        for i, features_dict in enumerate(features_list):
            try:
                result = cls.predict(features_dict)
                result["index"] = i
                results.append(result)
            except ValueError as e:
                results.append({
                    "index": i,
                    "error": str(e),
                    "prediction": None,
                    "label": None,
                })

        return results

    @staticmethod
    def _compute_confidence_level(confidence_score: float) -> str:
        """Convertit un score numérique en niveau de confiance qualitatif."""
        if confidence_score >= settings.CONFIDENCE_HIGH_THRESHOLD:
            return "Élevé"
        elif confidence_score >= settings.CONFIDENCE_LOW_THRESHOLD:
            return "Moyen"
        else:
            return "Faible"
