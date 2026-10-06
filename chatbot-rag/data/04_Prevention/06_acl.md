# Listes de contrôle d'accès (ACL - Access Control Lists)

## Introduction
Règles de sécurité configurées sur les équipements réseau pour filtrer le trafic en fonction des adresses IP, protocoles ou ports.

## Fiche Technique
| Type d'ACL | Éléments analysés | Avantage principal |
| :--- | :--- | :--- |
| **Standard** | IP Source uniquement | Traitement ultra-rapide |
| **Extended (Étendue)**| IP source/dest, protocoles, ports | Précision de filtrage |

## Explications détaillées
### Principe et Fonctionnement
Une liste de contrôle d'accès (ACL - Access Control List) est une suite ordonnée de règles d'autorisation ou d'interdiction (ex: `permit tcp any host 192.168.1.10 eq 80`, `deny ip any any`). Elles sont configurées directement sur les commutateurs de niveau 3 et les routeurs d'entreprise. Lorsqu'un paquet réseau arrive sur une interface de l'équipement, l'ACL est lue du haut vers le bas. Le paquet est traité par la première règle correspondante et les règles suivantes sont ignorées.

### Rôle dans la prévention DDoS
- **Filtrage à la frontière** : Bloquer immédiatement à l'entrée du réseau de l'entreprise des protocoles non autorisés (ex: bloquer tout trafic UDP entrant s'il n'y a pas de services UDP hébergés).
- **Blocage de blocs d'IP** : Rejeter des plages d'adresses IP entières identifiées comme malveillantes ou suspectes.

### Avantages et Limites
- **Avantages** :
  - Exécutées directement au niveau du processeur matériel (ASIC) des routeurs, les ACL n'ajoutent aucune latence et ne consomment pas de CPU logiciel.
  - Capables de gérer de très hauts débits (millions de paquets par seconde).
- **Limites** :
  - Rigides et difficiles à maintenir dynamiquement en temps réel lors d'une attaque distribuée.
  - Ne gèrent pas les informations de session ou le contexte applicatif (Couches L5/L7).

### Bonnes pratiques
1. Placer les règles de blocage les plus spécifiques en haut de l'ACL pour un traitement plus rapide.
2. Utiliser des ACL pour rejeter les adresses IP privées non routables (RFC 1918) arrivant sur l'interface WAN (Anti-Spoofing).

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
