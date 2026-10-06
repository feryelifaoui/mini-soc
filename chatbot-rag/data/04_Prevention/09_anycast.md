# Routage Anycast (Anycast Routing)

## Introduction
Technique d'adressage et de routage réseau permettant à plusieurs serveurs physiques de partager la même adresse IP publique.

## Fiche Technique
| Type de routage | Nombre de serveurs par IP | Distribution du trafic | Résilience DDoS |
| :--- | :--- | :--- | :--- |
| **Unicast** | 1 serveur / 1 IP | Tout le trafic converge vers un point unique | Faible (Point de défaillance unique) |
| **Anycast** | N serveurs / 1 IP | Le trafic est acheminé vers le point le plus proche | Très élevée (Distribution naturelle) |

## Explications détaillées
### Principe et Fonctionnement
Dans un réseau Anycast, plusieurs serveurs ou centres de données situés dans des régions géographiques différentes annoncent la même adresse IP publique en utilisant le protocole de routage **BGP** (Border Gateway Protocol). Les routeurs d'Internet acheminent automatiquement les paquets de l'utilisateur vers le serveur Anycast le plus proche "topologiquement" (le chemin réseau le plus court).

### Rôle dans la prévention DDoS
L'Anycast est la technologie fondamentale utilisée par les grands CDN (comme Cloudflare) et les serveurs DNS racine pour résister aux attaques DDoS massives :
- **Distribution de la charge** : L'attaque DDoS est géographiquement fragmentée. Si un botnet situé en Asie lance une attaque, le trafic d'attaque est naturellement dirigé et absorbé par les serveurs Edge Anycast situés en Asie, laissant les centres de données d'Europe et d'Amérique totalement épargnés et fonctionnels pour les utilisateurs locaux.
- **Résilience** : Si un centre de données Edge Anycast est saturé par une attaque locale, le protocole BGP met à jour les routes et redirige automatiquement le trafic vers le centre de présence opérationnel le plus proche.

### Avantages et Limites
- **Avantages** :
  - Absorption et distribution automatique de la charge d'attaque sans intervention manuelle.
  - Amélioration de la latence globale du site pour les utilisateurs légitimes.
- **Limites** :
  - Configuration réseau complexe au niveau BGP nécessitant des infrastructures réseau de niveau opérateur (AS - Autonomous System).

### Bonnes pratiques
1. Utiliser des fournisseurs de DNS basés sur une architecture Anycast pour garantir la résilience de la résolution de noms de domaine.
2. Associer Anycast à des mécanismes de nettoyage de trafic locaux dans chaque point de présence.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
