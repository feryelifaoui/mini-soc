# WAF (Web Application Firewall)

## Introduction
Pare-feu spécialisé de niveau applicatif (Couche 7) conçu pour protéger les applications web contre les attaques HTTP/HTTPS.

## Fiche Technique
| Métrique | Pare-feu traditionnel (L3/L4) | WAF (L7) |
| :--- | :--- | :--- |
| **Inspection** | Ports, IP sources, Flags TCP | En-têtes HTTP, Cookies, URL, Payload |
| **DDoS géré** | SYN Flood, UDP Flood | HTTP GET/POST Flood, Slowloris |
| **Chiffrement** | Ignore le contenu chiffré | Déchiffre et inspecte le HTTPS |

## Explications détaillées
### Principe et Fonctionnement
Un WAF (Web Application Firewall) est positionné devant les serveurs web pour inspecter le trafic HTTP et HTTPS en profondeur (Couche 7). Contrairement à un pare-feu traditionnel, le WAF comprend le protocole HTTP. Il analyse les en-têtes HTTP, les paramètres de requêtes GET/POST, les cookies, les requêtes JSON/XML et les formulaires. Il recherche des motifs d'attaques applicatives (telles que les injections SQL, XSS, mais aussi les comportements typiques des HTTP Floods et des bots automatisés).

### Rôle dans la prévention DDoS
Le WAF est indispensable contre les attaques applicatives (HTTP Flood, Slowloris). Il permet de :
- Identifier et bloquer les signatures d'outils d'attaque connus (ex. LOIC, requêtes HTTP malformées).
- Valider que le client est un navigateur réel en lui soumettant des défis (JavaScript silencieux, CAPTCHA).
- Appliquer des limites de requêtes par seconde (RPS) sur des pages critiques (formulaires de connexion, pages de recherche).

### Avantages et Limites
- **Avantages** :
  - Seule protection efficace pour filtrer finement le trafic web de couche 7.
  - Réduction drastique des requêtes malveillantes atteignant les serveurs applicatifs d'origine.
- **Limites** :
  - Nécessite le déchiffrement SSL/TLS (consomme du CPU).
  - Peut générer des faux positifs sur des flux d'API complexes.

### Bonnes pratiques
1. Déployer le WAF dans le cloud (Cloud-WAF) pour qu'il bénéficie d'une bande passante massive et filtre le trafic avant qu'il n'atteigne le datacenter de l'entreprise.
2. Utiliser des règles comportementales dynamiques plutôt que des règles de signatures statiques.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
