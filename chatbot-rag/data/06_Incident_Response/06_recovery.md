# Récupération et retour à la normale (Recovery Phase)

## Introduction
Rétablissement progressif et sécurisé des systèmes affectés, et surveillance accrue du trafic réseau.

## Fiche Technique
| Action de récupération | Risque associé | Mesure d'atténuation |
| :--- | :--- | :--- |
| **Retrait des filtres réseau** | Reprise immédiate de l'attaque | Effectuer le retrait par paliers |
| **Redémarrage des serveurs** | Surcharge due aux connexions en attente | Activer le rate limiting applicatif temporaire |
| **Changement DNS inverse** | Propagation lente du DNS (cache) | Réduire le TTL des enregistrements DNS |

## Explications détaillées
### Principe et Fonctionnement
La phase de récupération (Recovery) consiste à remettre en production les services qui ont été perturbés ou coupés pendant l'attaque DDoS, et à s'assurer qu'ils fonctionnent de manière stable et performante pour les utilisateurs. Cette phase doit être menée de manière méthodique pour éviter qu'une reprise brutale ne sature à nouveau les serveurs ou que l'attaquant ne relance immédiatement son assaut (effet de rebond).

### Processus de récupération progressive
- **Étape 1 : Rétablissement des flux** : Désactiver progressivement les règles de filtrage agressives du confinement (ex. retirer le Blackholing, restaurer le routage DNS d'origine).
- **Étape 2 : Redémarrage ordonné** : Redémarrer les services dans l'ordre de leurs dépendances (d'abord les bases de données, puis les serveurs d'applications internes, et enfin les serveurs web frontaux).
- **Étape 3 : Surveillance active** : Mettre en place un monitoring à haute fréquence du trafic réseau (PPS, BPS) et des performances CPU des serveurs pendant 24 à 48 heures.
- **Étape 4 : Validation utilisateur** : Effectuer des tests de fonctionnement (tests fonctionnels de bout en bout) pour s'assurer que les clients légitimes peuvent à nouveau utiliser l'application sans erreurs.

### Bonnes pratiques
1. Garder les équipes de sécurité en état d'alerte renforcée pendant la phase de reprise car les attaquants relancent souvent une deuxième vague d'attaque dès qu'ils voient le site remonter.
2. Mettre en cache un maximum de contenu lors du redémarrage pour réduire la charge immédiate sur les serveurs applicatifs backend.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
