<h1 align="center">🛡️ Mini SOC Intelligent</h1>

<p align="center">
  <strong>Un Security Operations Center (SOC) miniature, propulsé par l'Intelligence Artificielle et le Machine Learning.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LightGBM-000000?style=for-the-badge&logo=lgbm&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Ollama-ffffff?style=for-the-badge" />
</p>

## 📖 Présentation du Projet

**Mini SOC Intelligent** est une application complète conçue pour simuler les opérations essentielles d'un centre de sécurité (SOC). L'outil utilise des modèles d'apprentissage automatique pour détecter les cyberattaques (comme les attaques DDoS), ainsi qu'un agent IA (Chatbot RAG) capable d'assister les analystes en cybersécurité grâce à une base de connaissances métier.

### ✨ Fonctionnalités Principales

* **📊 Dashboard Analytique** : Interface utilisateur (Streamlit) pour monitorer les événements réseau.
* **🕵️ Détection DDoS (ML)** : Modèle `LightGBM` performant intégré pour repérer les anomalies et attaques DDoS dans le trafic réseau.
* **🤖 Assistant IA RAG** : Chatbot propulsé par `LangChain`, `FAISS` et `Ollama (Llama 3)` qui s'appuie sur une documentation interne pour aider les analystes à résoudre les incidents.
* **🚨 Système d'Alerte** : Envoi automatique de notifications par e-mail (via SMTP) lors de la détection de menaces critiques.
* **💾 Gestion des Incidents** : Base de données pour enregistrer, consulter et gérer l'historique des alertes (via FastAPI et SQL).

---

## 🛠️ Stack Technique

- **Frontend** : [Streamlit](https://streamlit.io/) (UI moderne et réactive)
- **Backend** : [FastAPI](https://fastapi.tiangolo.com/) (API robuste et rapide)
- **Machine Learning** : LightGBM (Détection), Pandas, Scikit-Learn
- **IA / NLP** : Ollama (modèles LLM en local, ex: Llama 3), LangChain, Base vectorielle FAISS
- **Base de données** : PostgreSQL / SQLite (via SQLAlchemy)

---

## 🏗️ Architecture du Répertoire

```text
📁 mini-soc/
│
├── 📂 backend/         # Logique métier, endpoints de l'API FastAPI, services d'email
├── 📂 frontend/        # Interface Streamlit (Dashboard, vues du Chatbot et de l'Agent)
├── 📂 chatbot-rag/     # Moteur RAG, index FAISS, documents Markdown et scripts PDF
├── 📂 database/        # Configuration SQL et initialisation de la base de données
├── 📂 modele ml/       # Modèle LightGBM pré-entraîné, notebooks, API ML indépendante
│
├── 📜 start_mini_soc.bat   # Script de démarrage rapide pour Windows
├── 📜 requirements.txt     # Dépendances du projet Python
└── 📜 README.md            # Ce fichier
```

---

## 🚀 Installation & Démarrage (Local)

### 1. Prérequis
- **Python 3.9+** installé sur votre machine.
- (Optionnel) **Ollama** installé et lancé localement pour le Chatbot RAG (avec un modèle comme `llama3`).

### 2. Configuration de l'environnement virtuel
Cloner ce dépôt puis configurer l'environnement :
```bash
git clone https://github.com/feryelifaoui/mini-soc.git
cd mini-soc

# Création et activation de l'environnement virtuel (Windows)
python -m venv venv
venv\Scripts\activate

# Installation des dépendances
pip install -r requirements.txt
```

### 3. Lancement Simplifié
Un script batch est inclus pour lancer simultanément l'API Backend et l'UI Frontend sous Windows.

Lancez le script depuis la racine du projet :
```bash
.\start_mini_soc.bat
```
*(Ou double-cliquez simplement sur `start_mini_soc.bat` depuis l'explorateur de fichiers).*

### 4. Accès aux Services
Une fois les services démarrés, vous pouvez y accéder via votre navigateur :
- 🎨 **Interface Utilisateur (SOC Dashboard)** : [http://localhost:8501](http://localhost:8501)
- ⚙️ **Backend API (Documentation Swagger)** : [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📧 Configuration des Alertes Email

Pour que le système d'alerte puisse envoyer des emails (ex: depuis un compte Gmail), vous devez configurer le mot de passe d'application SMTP dans vos variables d'environnement.

```env
SMTP_USER=votre_email@gmail.com
SMTP_PASSWORD=votre_mot_de_passe_application
```

---

## 🤝 Contribution
Ce projet est développé dans un cadre académique / expérimental. N'hésitez pas à forker le projet et à soumettre des Pull Requests si vous souhaitez ajouter de nouveaux modèles de détection (ex: Random Forest, Réseaux de Neurones) ou enrichir la base de connaissances du Chatbot.

## 📄 Licence
MIT License.
