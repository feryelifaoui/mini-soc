# Plan de continuité d'activité (PCA) et DDoS

## Introduction
Stratégie d'entreprise visant à maintenir le fonctionnement des activités essentielles en mode dégradé pendant une attaque DDoS majeure.

## Fiche Technique
| Processus métier | Impact de l'attaque DDoS | Procédure de contournement PCA |
| :--- | :--- | :--- |
| **Vente en ligne** | Site e-commerce inaccessible | Redirection temporaire vers une page d'attente avec numéro d'appel d'urgence |
| **Service Client** | Téléphonie IP et CRM coupés | Utilisation de téléphones mobiles professionnels et fichiers partagés cloud |
| **Facturation** | Logiciel ERP inaccessible | Enregistrement différé des écritures et saisie manuelle temporaire |

## Explications détaillées
### Principe et Fonctionnement
Le Plan de Continuité d'Activité (PCA) définit comment l'entreprise doit continuer à opérer lorsque ses outils informatiques principaux sont indisponibles. Alors que le département informatique s'efforce de résoudre l'attaque DDoS réseau, le reste de l'entreprise applique les procédures dégradées du PCA pour servir les clients et assurer les tâches quotidiennes indispensables.

### Composants d'un PCA face au déni de service
- **Identification des processus métiers critiques** : Déterminer quelles activités ne peuvent pas être interrompues pendant plus de quelques heures (ex: la chaîne d'expédition physique des colis sur un e-commerce).
- **Procédures manuelles et dégradées** : Décrire comment saisir les commandes clients sur papier ou via des outils bureautiques hors ligne si l'application web interne est inaccessible.
- **Systèmes de messagerie alternatifs** : Utiliser des plateformes collaboratives basées sur le cloud public (indépendantes du réseau de l'entreprise) pour maintenir la communication entre les équipes.

### Avantages et Limites
- **Avantages** :
  - Minimise l'impact financier et les retards de livraison pendant la crise.
  - Réduit la pression sur les équipes informatiques qui peuvent se concentrer sur la résolution technique sans subir le blocage total de l'entreprise.
- **Limites** :
  - Nécessite une formation régulière des employés non techniques aux procédures manuelles.

### Bonnes pratiques
1. Tester le PCA lors d'exercices d'indisponibilité réseau planifiés.
2. Conserver des copies physiques (papier) ou hors ligne sécurisées des annuaires de contacts d'urgence et des procédures clés.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
