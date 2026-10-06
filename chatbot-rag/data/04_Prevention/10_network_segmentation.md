# Segmentation réseau (Network Segmentation)

## Introduction
Division d'un réseau informatique en sous-réseaux isolés pour limiter la propagation des attaques et protéger les ressources critiques.

## Fiche Technique
| Zone de sécurité | Exposition Internet | Sensibilité des données | Protection type |
| :--- | :--- | :--- | :--- |
| **DMZ** | Oui (Publique) | Faible (ressources statiques) | Pare-feu externe, CDN, WAF |
| **Zone Applicative**| Non (Privée) | Moyenne (logique métier) | Pare-feu interne, IDS |
| **Zone Base de Données**| Non (Strictement privée) | Très élevée (données clients) | Isolation complète, chiffrement |

## Explications détaillées
### Principe et Fonctionnement
La segmentation réseau consiste à découper l'architecture réseau globale en plusieurs zones de sécurité distinctes (souvent via des **VLANs** ou des sous-réseaux IP) séparées par des pare-feux. Les flux de communication entre ces zones sont strictement réglementés et surveillés. Par exemple, une architecture classique comprend une zone DMZ (Demilitarized Zone) pour les serveurs web exposés à Internet, une zone applicative interne, et une zone de base de données isolée.

### Rôle dans la prévention DDoS
- **Confinement de l'attaque** : Si un serveur web situé dans la DMZ est saturé par une attaque DDoS applicative ou compromis, la segmentation réseau empêche l'attaque de se propager vers les bases de données internes ou le réseau bureautique des employés.
- **Préservation des services critiques** : Les communications internes essentielles (ex. Active Directory, messagerie interne) continuent de fonctionner normalement car elles empruntent des canaux réseau distincts de ceux saturés par le trafic internet public.

### Avantages et Limites
- **Avantages** :
  - Limite la surface d'exposition et empêche les mouvements latéraux des attaquants.
  - Facilite le diagnostic d'incident en isolant les segments perturbés.
- **Limites** :
  - Complexité de configuration et de maintenance des règles de pare-feu internes.

### Bonnes pratiques
1. Appliquer le principe du moindre privilège pour les flux inter-zones.
2. Isoler totalement le trafic de gestion d'infrastructure (Out-of-Band Management) sur un réseau physique ou logique dédié.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
