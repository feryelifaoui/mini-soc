# Attaque HTTPS Flood

## Introduction
Exploite le protocole HTTPS en forçant le serveur à effectuer des opérations de décryptage SSL/TLS intensives en ressources CPU.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 6 (Présentation) & 7 (Application) |
| **Protocole** | HTTPS (SSL/TLS sur TCP 443) |
| **Cible** | Processeur (CPU) du serveur web ou du terminateur SSL |
| **Impact CPU** | Extrêmement Élevé |
| **Bande passante requise** | Faible à Moyenne |

## Explications détaillées
### Principe et Fonctionnement
L'attaque HTTPS Flood combine une attaque HTTP Flood classique avec les contraintes de calcul du protocole SSL/TLS. Pour chaque connexion HTTPS entrante, le serveur doit effectuer une phase de "poignée de main" SSL/TLS (Handshake) qui implique des calculs cryptographiques complexes (déchiffrement des clés asymétriques). L'attaquant envoie des milliers de requêtes de négociation ou de renégociation SSL/TLS. Les ressources CPU du serveur sont rapidement épuisées par ces calculs intensifs, bien avant que les requêtes applicatives ne soient traitées par le serveur web.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Surcharge CPU immédiate du serveur web, impossibilité d'établir de nouvelles sessions HTTPS (Timeout lors de la négociation SSL), erreurs de certificat ou de connexion dans les navigateurs clients.
- **Indicateurs clés** :
  - Pics massifs de connexions sur le port TCP 443.
  - Nombre anormalement élevé de paquets de négociation TLS (`Client Hello`).
  - Utilisation intensive des ciphers cryptographiques gourmands en ressources par les clients.

### Détection, Prévention et Mitigation
- **Détection** :
  - Surveillance de l'utilisation du processeur dédiée aux processus cryptographiques.
  - Analyse des journaux du répartiteur de charge (Load Balancer) ou du proxy inverse.
- **Prévention** :
  - **SSL Offloading (Délestage SSL)** : Déporter la gestion du chiffrement/déchiffrement SSL/TLS sur un équipement dédié (Load Balancer matériel) ou un service cloud (CDN) situé en amont du serveur d'application.
  - Désactiver la renégociation SSL initiée par le client.
- **Mitigation** :
  - Filtrage IP géographique si l'attaque provient d'une région non ciblée par l'entreprise.
  - Utilisation de technologies comme le matériel cryptographique dédié (cartes d'accélération SSL) ou de processeurs modernes optimisés pour le TLS.

### Limites des protections
Le délestage SSL déplace la cible de l'attaque vers le CDN ou le Load Balancer. Bien que ces derniers disposent d'une capacité de traitement largement supérieure, ils peuvent tout de même être saturés si l'attaque est d'une envergure extrême.


## Exemple Concret
```nginx
# Désactiver la renégociation SSL initiée par le client sous Nginx
# (Nginx le gère nativement de manière sécurisée, mais on peut forcer les protocoles modernes)
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers on;
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque HTTPS Flood (Couche 7 (Application) / Couche 6 (Présentation)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
