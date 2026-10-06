# Proxy inverse (Reverse Proxy)

## Introduction
Serveur intermédiaire positionné devant les serveurs internes pour acheminer les requêtes des clients.

## Fiche Technique
| Outil Proxy | Mode de fonctionnement | Point fort face au DDoS |
| :--- | :--- | :--- |
| **Nginx** | Événementiel, asynchrone | Gestion de milliers de connexions TCP, cache performant |
| **HAProxy** | Orienté performances réseau | Répartition de charge L4/L7, limitation de débit |
| **Apache** | Processus / Threads | Richesse fonctionnelle mais plus lourd |

## Explications détaillées
### Principe et Fonctionnement
Un proxy inverse (Reverse Proxy) est un serveur d'intermédiation placé entre les clients externes et les serveurs d'applications internes (backend). Il reçoit les requêtes des clients, les valide, les traite éventuellement (compression, mise en cache, déchiffrement SSL) et les renvoie vers le serveur d'application adéquat. Les serveurs web comme Nginx, HAProxy ou Apache sont couramment configurés comme proxys inverses.

### Rôle dans la prévention DDoS
- **Isolation réseau** : Le proxy inverse sépare les serveurs d'applications sensibles d'Internet.
- **Gestion efficace des connexions TCP** : Nginx ou HAProxy utilisent des architectures événementielles non bloquantes capables de gérer simultanément des dizaines de milliers de connexions TCP ouvertes, protégeant ainsi les architectures backend plus fragiles (ex: serveurs Java, PHP, Node.js).
- **Limitation de débit** : Permet de configurer des filtres de requêtes par IP en frontal.

### Avantages et Limites
- **Avantages** :
  - Centralisation de la sécurité, du chiffrement TLS et de la répartition de charge.
  - Soulagement important des ressources des serveurs applicatifs backend.
- **Limites** :
  - S'il n'est pas redondé, le proxy inverse devient un point de défaillance unique (*Single Point of Failure*).

### Bonnes pratiques
1. Déployer Nginx ou HAProxy en cluster avec le protocole VRRP (Keepalived) pour assurer la haute disponibilité du proxy inverse lui-même.
2. Limiter la taille des en-têtes et du corps des requêtes entrantes pour éviter la surcharge mémoire.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
