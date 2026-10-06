# Attaque Slow POST (R-U-Dead-Yet ?)

## Introduction
Envoie des requêtes HTTP POST avec un en-tête Content-Length élevé mais transmet les données du corps de la requête octet par octet.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 7 (Application) |
| **Protocole** | HTTP / TCP |
| **Cible** | Thread pool et ressources d'attente du serveur d'application |
| **Impact CPU** | Très faible |
| **Bande passante requise** | Extrêmement faible |

## Explications détaillées
### Principe et Fonctionnement
Semblable à Slowloris, l'attaque Slow POST (souvent exécutée via l'outil RUDY - R-U-Dead-Yet) maintient les connexions au serveur web ouvertes le plus longtemps possible. L'attaquant envoie une requête HTTP `POST` valide, y compris les en-têtes complets, et spécifie dans l'en-tête `Content-Length` une taille de données très importante (ex: 1 million d'octets). Une fois le serveur prêt à recevoir le corps de la requête, l'attaquant commence à envoyer les données de manière extrêmement lente (ex: un seul octet toutes les 10 à 30 secondes). Le serveur web alloue des ressources mémoire et réseau pour attendre la totalité des données promises par l'en-tête `Content-Length`. En multipliant ces connexions lentes, l'attaquant épuise le pool de threads du serveur.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Épuisement des ressources réseau et des threads de traitement du serveur web, aucune consommation notable de bande passante globale.
- **Indicateurs clés** :
  - Présence de connexions HTTP POST actives n'envoyant pratiquement aucun octet par seconde.
  - File d'attente de traitement du serveur web saturée.

### Détection, Prévention et Mitigation
- **Détection** :
  - Surveillance des sockets réseau avec un débit de transfert de données quasi nul.
- **Prévention** :
  - Utilisation d'un proxy inverse en amont (Nginx, HAProxy) configuré pour mettre en mémoire tampon (bufferiser) le corps des requêtes HTTP entrantes avant de les transmettre au serveur d'application backend.
- **Mitigation** :
  - Configurer des limitations sur la taille maximale autorisée du corps des requêtes (`client_max_body_size` sous Nginx).
  - Réduire le timeout de réception du corps de la requête (`client_body_timeout` sous Nginx).

### Limites des protections
La bufferisation du corps des requêtes peut consommer de la mémoire RAM sur le proxy inverse si l'attaquant envoie de vrais gros fichiers. De plus, les applications légitimes nécessitant l'envoi de fichiers volumineux (ex: téléversement de vidéos) peuvent être impactées par des timeouts de corps de requête trop courts.


## Exemple Concret
```nginx
# Configuration Nginx pour limiter le timeout de réception du corps de la requête
client_body_timeout 10s;
client_header_timeout 10s;
keepalive_timeout 5s;
send_timeout 10s;
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque Slow POST (R-U-Dead-Yet ?) (Couche 7 (Application)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
