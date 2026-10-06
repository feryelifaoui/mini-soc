# Qu'est-ce qu'un DoS (Denial of Service) ?

## Introduction
Une attaque par déni de service (DoS - Denial of Service) est une tentative malveillante de rendre un service, une ressource réseau ou une machine indisponible pour ses utilisateurs légitimes. Contrairement aux intrusions ou au vol de données, l'objectif principal d'un DoS n'est pas de dérober des informations, mais d'interrompre le fonctionnement normal d'un système.

## Explications détaillées
Une attaque DoS s'effectue généralement depuis une seule source (une seule machine, une seule adresse IP) ciblant une victime unique. Elle repose sur deux principaux mécanismes d'action :

### 1. Inondation de ressources (Flooding)
L'attaquant envoie un volume de trafic (paquets réseau, requêtes applicatives) supérieur à ce que le système cible peut traiter. Les ressources matérielles (CPU, mémoire RAM) ou de bande passante réseau sont saturées, empêchant le traitement des requêtes légitimes.

### 2. Exploitation de vulnérabilités (Crash ou blocage)
L'attaquant envoie des paquets malformés ou des requêtes spécifiques conçues pour exploiter un bug dans le système d'exploitation ou une application de la cible (par exemple, l'attaque *Ping of Death* ou *Teardrop*). Cela provoque un plantage du système ou une boucle infinie de traitement, rendant le système inopérant instantanément sans nécessiter une bande passante importante.

### Caractéristiques techniques d'une attaque DoS
- **Source unique** : Une seule machine (serveur dédié, PC compromis) émet l'attaque.
- **Volume limité** : La puissance de l'attaque est limitée par les capacités de la machine de l'attaquant et de sa propre connexion Internet.
- **Facilité de blocage** : L'adresse IP de l'attaquant étant unique, il est relativement simple pour les pare-feux ou les administrateurs système de bloquer la source de l'attaque.

## Exemples concrets
- **Scénario d'inondation** : Un serveur web disposant d'une bande passante de 100 Mbps reçoit un flux continu de requêtes de 150 Mbps provenant d'une seule IP de serveur cloud. Le serveur ne peut plus répondre et les utilisateurs légitimes obtiennent des erreurs de type "Timeout".
- **Scénario d'exploitation** : L'envoi d'un paquet IP fragmenté invalide qui fait planter la pile TCP/IP d'un système d'exploitation Windows ou Linux non mis à jour (Blue Screen of Death).

## Synthèse des types de DoS
| Type de DoS | Mécanisme | Conséquence | Niveau de bande passante requis |
| :--- | :--- | :--- | :--- |
| **Volumétrique** | Inondation de paquets | Saturation réseau | Élevé |
| **Applicatif** | Requêtes HTTP complexes | Saturation CPU/Mémoire | Moyen à faible |
| **Vulnérabilité (Exploit)** | Paquet malformé | Crash système | Très faible |

## Avantages et limites de l'analyse DoS
### Avantages
- L'analyse d'une attaque DoS simple permet de comprendre les limites de performance d'un système unique.
- Permet d'identifier rapidement les vulnérabilités de code ou de configuration (ex. gestion des tampons mémoire).

### Limites
- Modèle obsolète pour les attaques à grande échelle modernes, car la plupart des attaques d'aujourd'hui sont distribuées (DDoS).

## Bonnes pratiques de défense
1. **Mises à jour régulières** : Appliquer les correctifs de sécurité pour éviter les plantages par exploitation de vulnérabilités.
2. **Filtrage à la source** : Bloquer immédiatement l'IP attaquante au niveau du pare-feu périmétrique (ACL).
3. **Limitation du débit (Rate Limiting)** : Configurer les serveurs pour rejeter les connexions excessives provenant d'une seule adresse IP.

## Conclusion
L'attaque DoS (Denial of Service) représente la forme originelle des attaques de déni de service. Bien qu'elle soit plus facile à bloquer et à atténuer qu'une attaque distribuée (DDoS), elle reste une menace pour les systèmes mal configurés ou non mis à jour. La compréhension du DoS est indispensable pour appréhender les concepts plus complexes du DDoS.