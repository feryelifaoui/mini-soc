# Attaque Slowloris

## Introduction
Maintient des milliers de connexions HTTP ouvertes en envoyant des requêtes partielles et extrêmement lentes.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 7 (Application) |
| **Protocole** | HTTP / TCP |
| **Cible** | Pool de connexions du serveur web |
| **Impact CPU** | Très faible |
| **Bande passante requise** | Extrêmement faible (< 1 Mbps) |

## Explications détaillées
### Principe et Fonctionnement
Slowloris est une attaque applicative particulièrement insidieuse et économe en bande passante. L'attaquant ouvre des connexions TCP avec le serveur web et envoie une requête HTTP (ex: `GET / HTTP/1.1`), mais n'envoie jamais les en-têtes HTTP de fin (marqués normalement par une double ligne vide `\r\n\r\n`). Pour maintenir la connexion active et éviter le timeout du serveur, l'attaquant envoie régulièrement des en-têtes supplémentaires bidons à intervalles réguliers (toutes les quelques secondes, ex: `X-a: b\r\n`). Le serveur web maintient le thread ou le processus alloué à cette connexion ouvert dans l'attente de la fin de la requête. Très rapidement, toutes les connexions disponibles du serveur web (le pool de threads) sont occupées par les sessions lentes de Slowloris, et les utilisateurs légitimes reçoivent des refus de connexion.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Le serveur web ne répond plus, mais les serveurs de base de données et le CPU du système restent inactifs ou peu sollicités. L'analyse réseau globale ne montre aucun pic de bande passante (l'attaque consomme moins de quelques kilobits par seconde).
- **Indicateurs clés** :
  - Nombre maximum de connexions simultanées atteint sur le serveur web.
  - Connexions actives bloquées pendant de très longues périodes avec des en-têtes incomplets.
  - Journaux d'accès web vides (les requêtes ne s'inscrivent dans l'access log qu'une fois finalisées).

### Détection, Prévention et Mitigation
- **Détection** :
  - Utilisation d'outils comme netstat ou ss pour voir le nombre de connexions établies avec de longs temps de maintien.
  - Analyse des connexions au niveau applicatif.
- **Prévention** :
  - Remplacer les serveurs web basés sur des threads par connexion (comme Apache en mode Prefork) par des serveurs événementiels (comme Nginx) capables de gérer des dizaines de milliers de connexions actives sans consommer de threads dédiés.
- **Mitigation** :
  - **Configuration des timeouts** : Réduire le temps d'attente maximum pour la réception des en-têtes HTTP (ex: `client_header_timeout` sous Nginx, `RequestReadTimeout` sous Apache).
  - Limiter le nombre de connexions simultanées par IP source.

### Limites des protections
Si les paramètres de timeout sont configurés de manière trop agressive, les utilisateurs légitimes disposant d'une connexion internet très lente ou instable (ex: connexions mobiles 3G/4G en zone rurale) peuvent voir leurs requêtes coupées avant d'avoir pu être transmises.


## Exemple Concret
```apache
# Configuration Apache (mod_reqtimeout) pour contrer Slowloris
<IfModule mod_reqtimeout.c>
  RequestReadTimeout header=20-40,MinRate=500 body=20,MinRate=500
</IfModule>
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque Slowloris (Couche 7 (Application)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
