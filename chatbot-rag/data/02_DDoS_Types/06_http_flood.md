# Attaque HTTP Flood

## Introduction
Surcharge les serveurs web avec des requêtes HTTP (GET/POST) imitant le comportement d'utilisateurs légitimes.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 7 (Application) |
| **Protocole** | HTTP / HTTPS |
| **Cible** | Serveur Web (Nginx, Apache), Application Backend, Base de données |
| **Impact CPU** | Très Élevé |
| **Bande passante requise** | Faible à Moyenne (l'attaque vise l'épuisement logique) |

## Explications détaillées
### Principe et Fonctionnement
Une attaque HTTP Flood cible la couche applicative (L7). L'attaquant envoie une multitude de requêtes HTTP `GET` ou `POST` vers le serveur web de la victime. Contrairement aux attaques de couche 4 (comme le SYN Flood), ces requêtes nécessitent une connexion TCP entièrement établie pour être transmises. Elles apparaissent donc comme du trafic légitime.
- **HTTP GET Flood** : Demande répétée de ressources lourdes (images volumineuses, fichiers PDF, pages nécessitant des calculs).
- **HTTP POST Flood** : Envoi répété de formulaires complexes ou de requêtes de recherche qui forcent le serveur à interroger sa base de données et à allouer des ressources d'écriture.
L'objectif est d'épuiser les threads du serveur web (ex: Apache, Nginx) et de saturer le serveur de base de données (ex: MySQL, PostgreSQL).

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Erreurs HTTP 502 Bad Gateway ou 504 Gateway Timeout, extrême lenteur de l'application web, processus du serveur web à 100% de CPU.
- **Indicateurs clés** :
  - Augmentation soudaine des requêtes par seconde (RPS) dans les logs d'accès du serveur web.
  - Taux anormal de requêtes provenant de la même adresse IP ou du même groupe d'IP (si non distribué).
  - Chaînes d'User-Agent identiques, suspectes ou obsolètes.

### Détection, Prévention et Mitigation
- **Détection** :
  - Analyse des journaux d'accès web (Access Logs) avec des outils SIEM ou des scripts d'analyse.
  - Surveillance du nombre de connexions HTTP actives par adresse IP.
- **Prévention** :
  - **Mise en cache agressive** : Utiliser un CDN pour servir toutes les pages statiques sans solliciter le serveur d'origine.
  - Utilisation d'un WAF (Web Application Firewall) pour analyser le comportement des requêtes.
- **Mitigation** :
  - **Rate Limiting** : Limiter le nombre de requêtes HTTP autorisées par adresse IP et par seconde (`limit_req` sous Nginx).
  - Déploiement de défis JavaScript ou de CAPTCHA (ex: Cloudflare "Under Attack" mode) pour filtrer les navigateurs automatisés (bots).
  - Blocage des User-Agents suspects.

### Limites des protections
Les attaquants avancés peuvent utiliser des navigateurs réels (via des frameworks d'automatisation comme Selenium ou Puppeteer) et distribuer l'attaque sur des milliers d'adresses IP résidentielles (proxys), rendant le filtrage par comportement très complexe.


## Exemple Concret
```nginx
# Exemple de configuration de limitation sous Nginx (nginx.conf)
limit_req_zone $binary_remote_addr zone=mylimit:10m rate=10r/s;

server {
    location / {
        limit_req zone=mylimit burst=20 nodelay;
        proxy_pass http://my_backend;
    }
}
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque HTTP Flood (Couche 7 (Application)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
