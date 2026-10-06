# Projet de Mini SOC Intelligent (Détection DDoS LOIC-HTTP)

Ce plan d'implémentation décrit la conception et le développement d'un mini SOC (Security Operations Center) intelligent. Le projet intègre de l'apprentissage automatique (Machine Learning) pour la détection en temps réel, une base de données relationnelle pour la persistance des alertes, un système de RAG (Retrieval-Augmented Generation) pour l'assistance cyber, et un Agent IA autonome orchestré avec rétroaction et apprentissage continu (Attack Patterns).

L'analyse de détection se basera spécifiquement sur le fichier :
[DDoS1-Tuesday-20-02-2018_TrafficForML_CICFlowMeter.parquet](file:///c:/Users/ferye/Desktop/stage/archive/DDoS1-Tuesday-20-02-2018_TrafficForML_CICFlowMeter.parquet)

---

## 👤 Choix Technologiques Validés

- **Modèle pour l'Agent IA & RAG** : Utilisation d'un LLM local via **Ollama** (ex: llama3, mistral ou autre modèle adapté).
- **Format des rapports** : Rapports d'incidents au format **Markdown** (fichiers `.md`).
- **Envoi des notifications** : Alertes et notifications par email via protocole **SMTP**.
- **Base PostgreSQL** : Déploiement en local ou via conteneur Docker.

---

## 📋 Plan de Projet en 20 Étapes (Livrables Concrets)

### Phase 1 — Préparation

#### Étape 1 — Analyse et Architecture du Projet
* **Objectif** : Définir clairement l'architecture globale et l'intégration du flux (Modèle ML ➔ Incident ➔ Agent IA ➔ RAG ➔ Humain ➔ AttackPatterns).
* **Action** : Établir le schéma détaillé des données et les interactions système.
* **Livrable** : Schéma d'architecture finalisé et liste figée des technologies.

#### Étape 2 — Installation de l'Environnement
* **Objectif** : Installer et isoler toutes les dépendances logicielles.
* **Action** : Créer l'environnement virtuel Python, configurer PostgreSQL et installer les bibliothèques requises (`pandas`, `numpy`, `scikit-learn`, `xgboost`, `fastapi`, `langchain`, `faiss-cpu`, `streamlit`, etc.).
* **Livrable** : Environnement opérationnel avec un script `requirements.txt`.

---

### Phase 2 — Machine Learning (Détection DDoS)

#### Étape 3 — Chargement et Validation du Dataset
* **Objectif** : Valider la conformité du fichier de données réseau ciblé.
* **Action** : Charger [DDoS1-Tuesday-20-02-2018_TrafficForML_CICFlowMeter.parquet](file:///c:/Users/ferye/Desktop/stage/archive/DDoS1-Tuesday-20-02-2018_TrafficForML_CICFlowMeter.parquet). Vérifier les types, la variable cible `Label` (`Benign` vs `DDoS attacks-LOIC-HTTP`).
* **Livrable** : Notebook Jupyter de validation et de chargement initial.

#### Étape 4 — Analyse Exploratoire des Données (EDA)
* **Objectif** : Modéliser le comportement des flux sains par rapport aux attaques LOIC-HTTP.
* **Action** : Générer des graphiques de distribution pour les caractéristiques clés (taille des paquets, nombre de paquets Forward, drapeaux TCP SYN/ACK).
* **Livrable** : Rapport EDA au format notebook contenant les visualisations clés.

#### Étape 5 — Prétraitement des Données
* **Objectif** : Nettoyer le dataset pour l'apprentissage.
* **Action** : Gérer les valeurs extrêmes ou infinies (ex. division par zéro dans les débits), encoder la cible (0 pour `Benign`, 1 pour `DDoS attacks-LOIC-HTTP`), et normaliser les caractéristiques.
* **Livrable** : Script de prétraitement reproductible et données nettoyées.

#### Étape 6 — Feature Engineering & Partitionnement
* **Objectif** : Préparer les ensembles d'entraînement et supprimer les colonnes non informatives.
* **Action** : Éliminer les 8 colonnes constantes (ex: `Bwd Avg Bulk Rate`). Effectuer une séparation stratifiée (Train, Validation, Test) pour préserver le ratio 60/40 de la cible.
* **Livrable** : Fichiers de données prêts pour l'entraînement.

#### Étape 7 — Entraînement et Comparaison de Modèles
* **Objectif** : Sélectionner l'algorithme le plus performant pour la détection DDoS.
* **Action** : Entraîner plusieurs classificateurs (Random Forest, XGBoost, LightGBM). Calculer et comparer l'Accuracy, le Recall, la Précision et le score F1.
* **Livrable** : Tableau comparatif des performances des modèles.

#### Étape 8 — Optimisation et Sauvegarde du Modèle
* **Objectif** : Ajuster les hyperparamètres et sérialiser le modèle.
* **Action** : Utiliser Optuna ou GridSearchCV pour optimiser le modèle XGBoost/Random Forest sélectionné. Sauvegarder sous `attack_detector.pkl`.
* **Livrable** : Fichier du modèle optimisé et prêt pour la production.

#### Étape 9 — API de Prédiction FastAPI
* **Objectif** : Exposer le modèle sous forme de service web temps réel.
* **Action** : Développer une API avec FastAPI qui reçoit en entrée les caractéristiques d'un flux réseau et renvoie la prédiction (`Benign` ou `DDoS`), la probabilité, et le niveau de confiance.
* **Livrable** : API FastAPI documentée (Swagger) et fonctionnelle.

---

### Phase 3 — Base de Données (PostgreSQL)

#### Étape 10 — Modélisation et Création de la Base PostgreSQL
* **Objectif** : Concevoir le schéma relationnel pour le suivi SOC.
* **Action** : Créer les tables `Users`, `Assets` (serveurs surveillés), `Incidents`, `Tickets` et la table d'apprentissage continu **`AttackPatterns`** (pour stocker les signatures d'attaques validées par l'admin).
* **Livrable** : Scripts SQL d'initialisation de la base de données.

#### Étape 11 — Gestion et Journalisation Automatique des Incidents
* **Objectif** : Enregistrer automatiquement les alertes dans la base.
* **Action** : Connecter l'API FastAPI à PostgreSQL pour insérer automatiquement une ligne dans `Incidents` à chaque fois qu'un flux est classifié comme `DDoS` avec un haut niveau de confiance.
* **Livrable** : Système d'insertion automatique d'incidents déclenché par les prédictions d'attaques.

---

### Phase 4 — RAG (Retrieval-Augmented Generation)

#### Étape 12 — Construction du Corpus Documentaire Cyber
* **Objectif** : Préparer la base de connaissances pour la remédiation.
* **Action** : Rassembler des guides de remédiation DDoS, de la documentation de pare-feu (Firewall), des configurations IDS, et des playbooks de réponses aux incidents (formats PDF/TXT/MD).
* **Livrable** : Dossier contenant le corpus de documents cyber.

#### Étape 13 — Indexation Vectorielle (FAISS)
* **Objectif** : Rendre la documentation interrogeable par similitude sémantique.
* **Action** : Écrire un script pour découper les documents (chunking), calculer les embeddings via `sentence-transformers`, et stocker le tout dans une base vectorielle FAISS.
* **Livrable** : Index vectoriel FAISS sauvegardé localement.

#### Étape 14 — Chatbot Cybersécurité RAG
* **Objectif** : Fournir une assistance contextuelle à l'analyste SOC.
* **Action** : Intégrer l'index FAISS avec LangChain pour répondre aux questions de l'utilisateur : *"Comment bloquer cette attaque ?"*, *"Quelle règle de firewall appliquer ?"*.
* **Livrable** : Moteur de chat sémantique (RAG) opérationnel.

---

### Phase 5 — Génération Automatique de Rapports

#### Étape 15 — Génération de Rapports d'Incidents
* **Objectif** : Automatiser la documentation administrative des attaques.
* **Action** : Écrire un module pour compiler les détails de l'incident (IP cible, horodatage, volume d'attaque, recommandations du RAG) et générer un rapport au format Markdown.
* **Livrable** : Script d'export de rapports d'incidents en Markdown.

---

### Phase 6 — Orchestration de l'Agent IA & Interface

#### Étape 16 — Conception de l'Agent IA (LangGraph)
* **Objectif** : Orchestrer le workflow du SOC de manière intelligente et autonome.
* **Action** : Créer un graphe d'agent où la détection d'une attaque déclenche séquentiellement la création d'incident, l'interrogation du RAG, la rédaction du rapport, et la planification de tickets.
* **Livrable** : Graphe d'agent IA défini et testé.

#### Étape 17 — Création Automatique de Tickets
* **Objectif** : Aligner les actions de remédiation avec un gestionnaire de tickets.
* **Action** : L'Agent IA crée automatiquement un ticket de remédiation dans la table `Tickets` avec une priorité, un statut (ex: Ouvert, En cours) et un assigné.
* **Livrable** : Module de création de tickets intégré à la base PostgreSQL.

#### Étape 18 — Envoi de Notifications (Emails/SMTP)
* **Objectif** : Alerter les administrateurs en cas d'attaque critique.
* **Action** : Configurer un service d'envoi d'emails (via SMTP) déclenché par l'Agent IA lors de la détection d'un incident de priorité élevée.
* **Livrable** : Système d'alerte mail opérationnel.

#### Étape 19 — Apprentissage Continu (Attack Patterns)
* **Objectif** : Permettre au système de s'adapter aux validations des analystes.
* **Action** : Créer une fonction de validation admin : si l'administrateur confirme l'attaque, le pattern (IP, signature de flux, drapeaux) est stocké dans la table `AttackPatterns`, converti en document textuel, puis injecté dynamiquement dans la base vectorielle du RAG pour enrichir la mémoire du SOC.
* **Livrable** : Pipeline de rétroaction et mise à jour de la mémoire du RAG.

#### Étape 20 — Interface Utilisateur Mini-SOC (Streamlit)
* **Objectif** : Proposer une console d'administration unifiée pour le SOC.
* **Action** : Développer une interface Streamlit affichant le tableau de bord des statistiques, la liste des incidents, le chatbot RAG, l'accès aux rapports exportés, la liste des tickets, et la section de validation des nouveaux Attack Patterns.
* **Livrable** : Interface web interactive Mini-SOC complète.

---

## 🧪 Plan de Vérification et Validation

### Tests Automatisés
- Écriture de tests unitaires pour l'API FastAPI (simuler l'envoi de paquets normaux et DDoS).
- Tests d'intégration pour le pipeline PostgreSQL et la création automatique d'incidents.

### Vérification Manuelle
- Lancement de l'interface Streamlit et déclenchement d'une fausse alerte DDoS pour vérifier le flux complet : détection ➔ incident ➔ ticket ➔ email ➔ chatbot RAG ➔ validation et enregistrement du pattern d'attaque.
