# Filtrage dynamique (Dynamic Filtering)

## Introduction
Ajustement automatique des règles de pare-feu et de blocage réseau en temps réel en réponse aux caractéristiques changeantes d'une attaque.

## Fiche Technique
| Type de filtrage | Mode de mise à jour | Réactivité aux attaques mutantes | Risque de faux positifs |
| :--- | :--- | :--- | :--- |
| **Statique** | Manuel (par un administrateur) | Faible (retard humain) | Faible |
| **Dynamique** | Automatique (script / IA) | Élevée | Moyen |

## Explications détaillées
### Principe et Fonctionnement
Le filtrage dynamique s'appuie sur des systèmes intelligents (souvent dotés d'algorithmes de Machine Learning ou de scripts d'automatisation réseau). Lors d'une attaque DDoS, le comportement des bots évolue fréquemment (les attaquants changent de ports, d'adresses IP sources, de types de requêtes ou de signatures d'User-Agent pour contourner les blocages). Le système de filtrage dynamique analyse le trafic entrant toutes les quelques secondes, détecte les nouvelles signatures d'attaque, écrit automatiquement des règles de pare-feu temporaires correspondantes, et supprime ces règles une fois que la signature de l'attaque disparaît.

### Rôle dans la mitigation DDoS
- **Adaptation automatique** : Permet de lutter contre les attaques multi-vectorielles et changeantes.
- **Minimisation des faux positifs** : Les règles de blocage ne sont appliquées que pendant la durée stricte du pic de trafic malveillant.

### Avantages et Limites
- **Avantages** :
  - Réduction de la charge de travail des analystes du SOC pendant la crise.
  - Réactivité accrue face aux changements de tactiques des attaquants.
- **Limites** :
  - Risque d'emballement des scripts d'automatisation (si le trafic légitime est mal interprété, le système peut écrire une règle bloquant vos propres clients).

### Bonnes pratiques
1. Configurer des garde-fous stricts dans les scripts de filtrage dynamique (ex. ne jamais autoriser le script à bloquer des plages d'IP internes ou des adresses DNS racine).
2. Logger précisément chaque modification de règle pare-feu effectuée par le système.

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
