# Haute disponibilité (High Availability)

## Introduction
Conception de système garantissant un niveau de performance opérationnelle et de disponibilité élevé sur une période donnée (les 'neufs').

## Fiche Technique
| Niveau de disponibilité | Temps d'indisponibilité max / an | Classification |
| :--- | :--- | :--- |
| **99% ("Deux neufs")** | 3.65 jours | Standard |
| **99.9% ("Trois neufs")**| 8.76 heures | Haute Disponibilité |
| **99.99% ("Quatre neufs")**| 52.6 minutes | Très Haute Disponibilité |
| **99.999% ("Cinq neufs")**| 5.26 minutes | Critique / Militaire |

## Explications détaillées
### Principe et Fonctionnement
La haute disponibilité (HA - High Availability) est une approche globale d'ingénierie visant à éliminer les points de défaillance uniques (*Single Points of Failure - SPOF*). Elle repose sur trois principes fondamentaux :
1. **La redondance** : Doubler ou tripler chaque composant critique de l'infrastructure (liaisons internet, routeurs, pare-feux, serveurs, alimentations électriques).
2. **Le basculement automatique (Failover)** : Capacité du système à détecter instantanément la panne d'un composant et à basculer le trafic vers le composant redondant sans interruption pour les utilisateurs.
3. **La réplication des données** : S'assurer que les bases de données et les fichiers sont synchronisés en temps réel sur les différents nœuds.

### Rôle dans la prévention DDoS
Face à une attaque DDoS protocolaire ou applicative qui fait planter un composant spécifique de l'architecture, la haute disponibilité garantit que l'activité globale ne s'arrête pas. Le trafic est automatiquement dérouté vers les composants sains du cluster, limitant ainsi l'impact pour les clients.

### Avantages et Limites
- **Avantages** :
  - Résilience globale de l'entreprise face aux pannes matérielles et aux cyberattaques.
  - Minimise le coût financier de l'indisponibilité.
- **Limites** :
  - Coût d'infrastructure et de licences multiplié par deux ou trois.
  - Complexité de configuration accrue (risques de désynchronisation de données).

### Bonnes pratiques
1. Définir des objectifs de disponibilité réalistes (ex. 99.9% ou 99.99%) associés à des plans de secours testés.
2. Réaliser des tests de basculement réguliers en production (Chaos Engineering).

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
