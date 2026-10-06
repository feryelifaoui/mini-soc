# 🛡️ DDoS Detection API — FastAPI + LightGBM

API REST de détection d'attaques DDoS (LOIC-HTTP) pour Mini-SOC, construite avec **FastAPI** et un modèle **LightGBM** entraîné sur des captures réseau CICFlowMeter.

---

## 📁 Structure du projet

```
stage/
├── ddos_lightgbm.ipynb          # Notebook d'entraînement du modèle
├── ddos_lgb_model.pkl           # Modèle sérialisé (généré par le notebook)
├── model_metadata_lgb.json      # Métadonnées du modèle (features, métriques)
├── generate_demo_model.py       # Script pour générer un modèle de test rapide
│
└── api/                         # 📦 API FastAPI
    ├── main.py                  # Application principale
    ├── run.py                   # Script de démarrage
    ├── requirements.txt         # Dépendances Python
    └── app/
        ├── core/
        │   ├── config.py        # Configuration (chemins, seuils)
        │   └── model.py         # Singleton ModelManager (chargement + inférence)
        ├── routers/
        │   ├── predict.py       # POST /api/v1/predict
        │   ├── batch.py         # POST /api/v1/predict/batch
        │   └── health.py        # GET  /api/v1/health | /api/v1/model/info
        └── schemas/
            └── schemas.py       # Modèles Pydantic (entrées/sorties)
```

---

## 🚀 Installation et Démarrage

### 1. Prérequis

```bash
pip install -r api/requirements.txt
```

### 2. Entraîner le modèle (ou utiliser le modèle de démonstration)

**Option A — Modèle réel** (recommandé) :
```bash
# Exécutez toutes les cellules du notebook
jupyter notebook ddos_lightgbm.ipynb
```

**Option B — Modèle de démonstration** (test rapide) :
```bash
python generate_demo_model.py
```

### 3. Lancer l'API

```bash
cd api
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Accéder à la documentation Swagger

| Interface | URL |
|-----------|-----|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| OpenAPI JSON | http://localhost:8000/openapi.json |

---

## 📡 Endpoints

### `GET /` — Accueil
Informations générales sur l'API.

### `GET /api/v1/health` — Health Check
Vérifie l'état du modèle et de l'API. Utilisé pour le monitoring SOC.

```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_name": "LightGBM DDoS Detector (LOIC-HTTP)",
  "selected_features": ["Dst Port", "Protocol", ...],
  "metrics": {"Accuracy": 0.99, "Recall": 0.99, ...},
  "message": "API et modèle LightGBM opérationnels."
}
```

### `GET /api/v1/model/info` — Informations du modèle
Retourne les hyperparamètres, features sélectionnées, features exclues et métriques de performance.

### `POST /api/v1/predict` — Prédiction unitaire ⭐

Analyse un flux réseau et retourne la prédiction DDoS.

**Corps de la requête :**
```json
{
  "Dst Port": 80.0,
  "Protocol": 6.0,
  "Flow Duration": 100000.0,
  "Total Fwd Packets": 5000.0,
  "SYN Flag Count": 5000.0,
  ...
}
```

**Réponse :**
```json
{
  "prediction": 1,
  "label": "DDoS",
  "ddos_probability": 0.9874,
  "benign_probability": 0.0126,
  "confidence_score": 0.9874,
  "confidence_level": "Élevé",
  "alert": true,
  "alert_message": "🚨 ALERTE : Attaque DDoS détectée avec une confiance Élevé (98.74%)"
}
```

### `POST /api/v1/predict/batch` — Prédiction en lot 📦

Analyse jusqu'à **1000 flux réseau** simultanément.

```json
{
  "flows": [
    {"Dst Port": 80.0, "Protocol": 6.0, ...},
    {"Dst Port": 443.0, "Protocol": 6.0, ...}
  ]
}
```

**Réponse :**
```json
{
  "total_flows": 2,
  "ddos_count": 1,
  "benign_count": 1,
  "error_count": 0,
  "ddos_percentage": 50.0,
  "summary": "⚠️ ATTENTION : 1/2 flux (50.0%) suspects détectés.",
  "results": [...]
}
```

---

## 🎯 Niveaux de confiance

| Score | Niveau | Signification |
|-------|--------|---------------|
| ≥ 85% | **Élevé** | Prédiction très fiable — Action SOC immédiate |
| 60–85% | **Moyen** | Prédiction probable — Investigation recommandée |
| < 60% | **Faible** | Incertitude élevée — Analyse manuelle nécessaire |

---

## 🔧 Configuration

Modifiez `api/app/core/config.py` ou créez un fichier `.env` dans `api/` :

```env
MODEL_PATH=C:/chemin/vers/ddos_lgb_model.pkl
METADATA_PATH=C:/chemin/vers/model_metadata_lgb.json
API_PORT=8000
CONFIDENCE_LOW_THRESHOLD=0.60
CONFIDENCE_HIGH_THRESHOLD=0.85
```

---

## 🧪 Test avec curl

```bash
# Health Check
curl http://localhost:8000/api/v1/health

# Prédiction unitaire (DDoS)
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"Dst Port": 80, "Protocol": 6, "Total Fwd Packets": 5000, "SYN Flag Count": 5000}'

# Prédiction batch
curl -X POST http://localhost:8000/api/v1/predict/batch \
  -H "Content-Type: application/json" \
  -d '{"flows": [{"Dst Port": 80, "Protocol": 6, "Total Fwd Packets": 5000, "SYN Flag Count": 5000}]}'
```

---

## ⚠️ Features exclues (risque d'overfitting)

Les features suivantes sont **intentionnellement exclues** du modèle car elles sont trop parfaites dans les données de laboratoire et causent un surapprentissage :

- `Flow Byts/s`
- `Flow Pkts/s`  
- `Fwd Pkts/s`
- `Bwd Pkts/s`

---

## 📊 Métriques du modèle réel (après exécution du notebook)

| Métrique | Valeur |
|----------|--------|
| Accuracy | > 99% |
| Recall (Taux Détection) | > 99% |
| Precision | > 99% |
| F1-Score | > 99% |
| FAR (Fausse Alerte) | < 1% |
| ROC-AUC | > 99% |
