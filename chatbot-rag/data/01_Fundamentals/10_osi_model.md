# Le modèle OSI et son importance en cybersécurité DDoS

## Introduction
Le modèle OSI (Open Systems Interconnection) décrit le fonctionnement des communications réseau en 7 couches. Il permet de classer les attaques DDoS selon la couche ciblée afin d'appliquer la bonne contre-mesure.

## Explications détaillées

### Les 7 couches du modèle OSI appliquées au DDoS

- **Couche 1 : Physique (Physical)** : Transmission brute. DDoS rare (coupure de câbles).
- **Couche 2 : Liaison (Data Link)** : Adressage physique (MAC). DDoS type MAC Flooding sur le LAN.
- **Couche 3 : Réseau (Network)** : IP. DDoS type ICMP Flood, fragmentation (saturation CPU pare-feu/routeurs).
- **Couche 4 : Transport (Transport)** : TCP/UDP. DDoS type SYN Flood, UDP Flood (saturation bande passante et tables d'état).
- **Couche 5 : Session (Session)** : Sessions de communication. DDoS ciblant le handshaking SSL/TLS.
- **Couche 6 : Présentation (Presentation)** : Traduction et chiffrement. DDoS par négociation SSL intensive.
- **Couche 7 : Applicative (Application)** : HTTP, DNS. DDoS type HTTP Flood, Slowloris (saturation serveurs web et bases de données).

## Tableau récapitulatif des attaques par couche OSI
| Couche OSI | Protocole ciblé | Type d'attaque typique | Équipement de protection adapté |
| :--- | :--- | :--- | :--- |
| **Couche 3 (Réseau)** | IP, ICMP | ICMP Flood, IP Fragmentation | Routeur (ACL), Pare-feu périmétrique |
| **Couche 4 (Transport)** | TCP, UDP | SYN Flood, UDP Flood | Pare-feu (SYN Cookies), Cloud Scrubbing |
| **Couche 7 (Application)** | HTTP, HTTPS, DNS | HTTP Flood, Slowloris, DNS Query | WAF (Web Application Firewall), CDN |

## Avantages et limites de l'analyse OSI
### Avantages
- Fournit une grille de diagnostic claire.
- Oriente vers le bon équipement de défense (ex: WAF pour couche 7).

### Limites
- Les attaques modernes combinent souvent plusieurs couches (ex. volumétrique L4 et applicatif L7) simultanément.

## Bonnes pratiques de défense
1. **Défense en profondeur** : Déployer des protections à chaque couche.
2. **Corrélation des logs** : Corréler NetFlow (L3/L4) et logs applicatifs (L7) pour identifier les attaques combinées.

## Conclusion
Le modèle OSI structure la défense DDoS en associant chaque attaque à sa couche. Identifier la couche visée permet de déployer immédiatement la contre-mesure réseau ou applicative adéquate.