# Limitation du débit (Rate Limiting)

## Introduction
Technique de sécurité consistant à limiter le nombre d'actions ou de requêtes qu'un utilisateur ou une IP peut effectuer dans un intervalle de temps donné.

## Fiche Technique
| Algorithme | Fonctionnement | Cas d'usage type |
| :--- | :--- | :--- |
| **Token Bucket** | Accumulation de jetons dans un réservoir | Autorise des rafales de trafic (burst) temporaires |
| **Leaky Bucket** | File d'attente à débit d'écoulement fixe | Lissage strict du trafic réseau |
| **Fixed Window** | Compteur sur une période fixe (ex: 1 min) | Simple à coder mais vulnérable aux pics aux frontières |

## Explications détaillées
### Principe et Fonctionnement
Le Rate Limiting consiste à définir des quotas stricts d'utilisation des ressources. Par exemple, le système peut autoriser un maximum de 60 requêtes HTTP par minute pour une même adresse IP. Si cette limite est dépassée, le serveur rejette les requêtes supplémentaires en renvoyant un code d'erreur HTTP `429 Too Many Requests`. Cette méthode est souvent implémentée via des algorithmes comme le *Token Bucket* ou le *Leaky Bucket*.

### Rôle dans la prévention DDoS
- Bloquer les attaques par force brute et les HTTP Floods de faible intensité émis par des sources uniques.
- Protéger les points d'accès API critiques contre l'abus et l'épuisement des ressources backend.

### Avantages et Limites
- **Avantages** :
  - Simple à mettre en œuvre au niveau du serveur web (Nginx), de la passerelle d'API (API Gateway) ou du code de l'application.
  - Évite qu'un seul utilisateur malveillant ou mal configuré ne monopolise les ressources du serveur.
- **Limites** :
  - Inefficace contre les attaques DDoS massives hautement distribuées (si l'attaque utilise 100 000 IP différentes, chaque IP peut envoyer 1 seule requête par minute et contourner la limite tout en saturant collectivement le serveur).

### Bonnes pratiques
1. Appliquer des seuils différents selon la sensibilité de l'URL (ex. plus strict sur `/login` ou `/search` que sur `/static/`).
2. Configurer des alertes pour notifier l'équipe de sécurité lorsqu'une IP dépasse fréquemment les seuils.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
