# Protocoles réseau importants et vulnérabilités DDoS

## Introduction
Certains protocoles possèdent des faiblesses structurelles que les attaquants exploitent pour mener des attaques DDoS. L'étude de ces protocoles permet de comprendre comment ils sont détournés.

## Explications détaillées

### 1. DNS (Domain Name System)
Traduit les domaines en IP (UDP 53).
- **Vulnérabilité** : Fonctionne sur UDP, permettant l'IP Spoofing.
- **Détournement (Amplification)** : Envoi de petites requêtes (ANY) avec l'IP usurpée de la victime à des résolveurs ouverts. Les serveurs répondent massivement à la victime.

### 2. NTP (Network Time Protocol)
Synchronise les horloges (UDP 123).
- **Détournement (Amplification)** : La commande `monlist` renvoie la liste des 600 dernières IP. Une petite requête génère une réponse massive envoyée à la victime.

### 3. SSDP (Simple Service Discovery Protocol)
Découverte de périphériques UPnP (UDP 1900).
- **Détournement** : Interrogé depuis Internet avec l'IP source de la victime pour générer des flux saturants.

### 4. ICMP (Internet Control Message Protocol)
Informations opérationnelles (Ping).
- **Détournement** : Le *ICMP Flood* sature les liens ou force le serveur à renvoyer des réponses, consommant son processeur.

## Tableau des protocoles et facteurs d'amplification
| Protocole | Port standard | Mode de transport | Commande exploitée | Facteur d'amplification |
| :--- | :--- | :--- | :--- | :--- |
| **DNS** | 53 | UDP | Requête ANY / DNSSEC | x20 à x100 |
| **NTP** | 123 | UDP | Commande `monlist` | x500 à x600 |
| **SSDP** | 1900 | UDP | Requête M-SEARCH | x30 |
| **Memcached**| 11211 | UDP | Lecture de clé de cache | x10 000 à x51 000 |
| **ICMP** | N/A | IP | Echo Request | Pas d'amplification (x1) |

## Bonnes pratiques de sécurisation
1. **Désactiver les commandes obsolètes** : Désactiver `monlist` dans la configuration NTP (mise à jour NTP).
2. **Désactiver UPnP/SSDP sur le WAN** : S'assurer que les routeurs n'exposent pas le port 1900.
3. **Sécuriser les résolveurs DNS** : Empêcher les requêtes récursives provenant d'Internet.
4. **Rate Limiting ICMP** : Limiter le débit d'ICMP au niveau des pare-feux.

## Conclusion
Les vulnérabilités liées aux protocoles résident dans l'absence de session UDP et l'asymétrie des paquets. Sécuriser ces protocoles exige une configuration stricte et le blocage des fonctionnalités obsolètes.