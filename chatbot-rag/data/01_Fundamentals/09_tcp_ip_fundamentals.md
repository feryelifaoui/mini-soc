# Rappels TCP/IP pour la sécurité DDoS

## Introduction
TCP/IP (Transmission Control Protocol / Internet Protocol) est le socle d'Internet. Une expertise de TCP/IP est indispensable pour comprendre la mécanique fine des attaques DDoS réseau et transport (couches 3 et 4).

## Explications détaillées

### 1. Le protocole IP (Internet Protocol) - Couche 3
IP est responsable de l'adressage et du routage.
- **L'adresse IP source** : Ne dispose d'aucun mécanisme natif de vérification. Les attaquants pratiquent l'usurpation d'adresse (**IP Spoofing**) sur UDP.
- **La fragmentation IP** : Si un paquet dépasse la MTU, il est découpé. Les attaquants exploitent cela en envoyant des fragments malformés (ex: attaque *Teardrop*).

### 2. Le protocole TCP - Couche 4
TCP est orienté connexion et fiable. Il nécessite le Three-Way Handshake :
1. **SYN** : Le client envoie une demande d'ouverture.
2. **SYN-ACK** : Le serveur confirme et envoie sa propre séquence.
3. **ACK** : Le client valide. La connexion passe à l'état `ESTABLISHED`.

Les drapeaux (Flags) TCP majeurs sont SYN, ACK, FIN, RST, PSH, URG.

### 3. Le protocole UDP - Couche 4
UDP est sans connexion et léger. L'absence de poignée de main rend l'IP Spoofing trivial, faisant d'UDP le protocole privilégié pour les attaques volumétriques par amplification (DNS, NTP).

## Tableau des caractéristiques TCP vs UDP
| Caractéristique | TCP | UDP |
| :--- | :--- | :--- |
| **Orientation** | Orienté connexion | Sans connexion |
| **Fiabilité** | Oui | Non |
| **IP Spoofing** | Difficile bidirectionnel | Très facile |
| **Attaque DDoS type** | SYN Flood, ACK Flood, Slowloris | UDP Flood, Amplification DNS/NTP |
| **Goulot d'étranglement**| CPU, Table d'états (Backlog, Firewall) | Bande passante réseau |

## Bonnes pratiques de sécurité réseau
1. **Activer les SYN Cookies** : Évite de stocker l'état de la connexion dans le backlog lors du SYN.
2. **Filtrer le trafic usurpé (BCP 38 / RFC 2827)** : Les FAI doivent empêcher la sortie de paquets à IP source usurpée.
3. **Limiter les fragments IP** : Configurer les pare-feux pour rejeter les fragments IP suspects.

## Conclusion
La pile TCP/IP est le terrain des attaques DDoS volumétriques et protocolaires. Sa maîtrise permet la mise en place de filtrages efficaces comme les SYN Cookies ou les règles BCP 38.