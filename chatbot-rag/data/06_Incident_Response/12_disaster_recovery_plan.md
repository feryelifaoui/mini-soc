# Plan de reprise d'activité (PRA) et DDoS

## Introduction
Planification technique décrivant la reconstruction et la restauration complète de l'infrastructure informatique suite à une interruption majeure.

## Fiche Technique
| Métrique PRA | Définition | Objectif type face au DDoS |
| :--- | :--- | :--- |
| **RTO** | Délai maximal de reprise du service | Moins de 4 heures (pour les services critiques) |
| **RPO** | Perte de données maximale acceptable | Proche de 0 (sauvegardes en temps réel répliquées) |
| **DR Site (Site PRA)**| Centre de données secondaire de secours | Actif / Passif ou Actif / Actif |

## Explications détaillées
### Principe et Fonctionnement
Le Plan de Reprise d'Activité (PRA) est un document purement technique rédigé par la direction informatique (DSI) et l'équipe réseau. Il décrit la procédure étape par étape pour reconstruire et restaurer le système d'information de l'entreprise après un désastre ou une cyberattaque destructrice. Dans le contexte du DDoS, le PRA s'applique si l'attaque a provoqué des dommages matériels (crash d'équipements de sécurité) ou si l'infrastructure d'origine doit être déplacée en urgence vers un site de secours (Backup/DR Site).

### Éléments d'un PRA face au DDoS
- **Objectif de temps de récupération (RTO - Recovery Time Objective)** : Temps maximum acceptable pour rétablir les services après la coupure.
- **Objectif de point de récupération (RPO - Recovery Point Objective)** : Perte de données maximale acceptable (ex. restaurer la base de données à son état de la veille).
- **Restauration à partir des sauvegardes** : Procédure de déploiement des sauvegardes d'applications et de configurations sur du matériel de secours vierge.
- **Bascule vers le site de secours (Failover)** : Modification des enregistrements DNS mondiaux ou des routes BGP pour faire pointer l'adresse IP publique de l'entreprise vers le centre de données secondaire.

### Avantages et Limites
- **Avantages** :
  - Assure la résilience de l'entreprise même face à un effondrement complet du datacenter principal.
- **Limites** :
  - Maintenir un site de secours complet (PRA synchrone) est extrêmement coûteux en infrastructures de serveurs et en liaisons réseau dédiées.

### Bonnes pratiques
1. Automatiser le processus de bascule (Failover) à l'aide de solutions de gestion de trafic global (GSLB).
2. Tester le PRA au moins une fois par an en simulant une panne totale du site de production principal.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
