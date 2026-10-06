# Architecture client-serveur et DDoS

## Introduction
Le réseau Internet repose sur le modèle d'architecture client-serveur. Comprendre cette architecture est fondamental pour analyser comment les attaques DDoS exploitent le déséquilibre entre client et serveur.

## Explications détaillées

### 1. Le modèle Client-Serveur
- **Le Client** : Initie une demande de service en envoyant une requête réseau.
- **Le Serveur** : Écoute en permanence sur des ports réseau (80, 443). Reçoit la requête, la traite et renvoie une réponse.

### 2. L'asymétrie exploitée par le DDoS
L'architecture présente une asymétrie en faveur du client :
- **Coût de la requête** : Très peu de ressources pour le client.
- **Coût du traitement** : CPU, mémoire RAM, accès disque et base de données pour le serveur.
En coordonnant des milliers de clients malveillants, l'attaquant force le serveur à saturer ses ressources physiques.

### 3. Points de défaillance face au DDoS
- **La file d'attente TCP (Backlog queue)** : Stocke les connexions semi-ouvertes. Sature rapidement en cas de SYN Flood.
- **Le serveur web (Nginx, Apache)** : Chaque connexion consomme un thread. Le dépassement de la configuration max bloque le serveur.
- **La base de données** : Les requêtes dynamiques saturent les processeurs de la base.

## Tableau des limites de l'architecture client-serveur
| Composant | Goulot d'étranglement | Impact de la saturation |
| :--- | :--- | :--- |
| **Pile Réseau OS** | File d'attente TCP Backlog | Rejet immédiat de nouvelles connexions TCP |
| **Serveur Web** | Nombre de processus/threads max | Connexions en attente ou erreurs HTTP 503 |
| **Base de Données** | Verrous de table, Pool de connexions | Requêtes SQL en attente (timeout) |
| **Bande Passante** | Capacité du port réseau physique | Perte de paquets en entrée (Packet loss) |

## Bonnes pratiques de conception
1. **Mettre en place un proxy inverse (Reverse Proxy)** : HAProxy ou Nginx pour gérer efficacement des milliers de connexions TCP simultanées.
2. **Utiliser la mise en cache (Caching)** : Placer les ressources statiques sur un CDN.
3. **Limitation dynamique des connexions** : Limiter le nombre de connexions autorisées par IP client unique.

## Conclusion
Le modèle client-serveur est structurellement asymétrique. Sécuriser cette architecture nécessite d'interposer des couches de cache, de répartition de charge et de filtrage.