# Confinement de l'incident (Containment Phase)

## Introduction
Actions immédiates pour limiter l'impact de l'attaque DDoS et isoler les parties saines du réseau.

## Fiche Technique
| Méthode de confinement | Vitesse d'effet | Impact sur le trafic légitime | Niveau de complexité |
| :--- | :--- | :--- | :--- |
| **Redirection Cloud** | Moyenne (Minutes) | Faible (filtrage fin) | Moyen |
| **Blocage de port (ACL)** | Instantanée | Moyen (si port partagé) | Faible |
| **Null Routing (Blackhole)**| Instantanée | Élevé (site coupé) | Faible |

## Explications détaillées
### Principe et Fonctionnement
Le confinement (ou endiguement) vise à stopper la propagation des effets de l'attaque DDoS et à éviter que d'autres services informatiques de l'entreprise ne s'effondrent. C'est une phase d'action d'urgence où la cellule de crise déploie des barrières réseau temporaires.

### Stratégies de confinement face au DDoS
- **Activation de la protection Cloud (Redirection DNS/BGP)** : Dérouter l'ensemble du trafic internet entrant vers le fournisseur cloud de nettoyage (Scrubbing Center) pour séparer les flux.
- **Règles ACL périmétriques d'urgence** : Bloquer les ports et protocoles identifiés lors de l'analyse (ex: bloquer tout trafic UDP sur le port 123 s'il s'agit d'une amplification NTP).
- **Rate Limiting agressif** : Brider drastiquement le trafic non essentiel ou non authentifié pour préserver la connectivité des services clés (ex. base de données clients).
- **Isolement de sous-réseaux (Segmentation)** : Couper physiquement ou logiquement les connexions réseau entre le segment internet saturé (DMZ) et le cœur de réseau interne de l'entreprise.

### Bonnes pratiques
1. Avoir des scripts de configuration pare-feu et des playbooks pré-rédigés pour un déploiement rapide.
2. Valider l'impact sur le trafic légitime avant d'appliquer des règles de confinement agressives.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
