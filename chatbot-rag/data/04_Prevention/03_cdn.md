# CDN (Content Delivery Network)

## Introduction
Réseau de serveurs géographiquement distribués collaborant pour fournir rapidement du contenu web aux utilisateurs.

## Fiche Technique
| CDN Edge Server | Serveur d'origine (Origin) |
| :--- | :--- |
| **Emplacement** | Partout dans le monde (distribué) | Datacenter de l'entreprise (centralisé) |
| **Contenu servi** | Contenu statique en cache | Requêtes dynamiques, bases de données |
| **Bande passante** | Très élevée (Échelle Tbps) | Limitée (Échelle Gbps ou Mbps) |

## Explications détaillées
### Principe et Fonctionnement
Un CDN (Content Delivery Network) est un grand réseau de serveurs relais (appelés serveurs Edge ou points de présence - PoPs) répartis dans le monde entier. Le CDN met en cache les ressources statiques d'un site web (images, fichiers HTML/CSS/JS, vidéos) sur ces serveurs Edge. Lorsqu'un utilisateur demande une page web, le CDN la sert depuis le serveur Edge le plus proche géographiquement.

### Rôle dans la prévention DDoS
Le CDN offre une protection intrinsèque contre le DDoS volumétrique :
- **Absorption massive** : La bande passante totale d'un CDN mondial (ex: Cloudflare, Akamai) se chiffre en centaines de térabits par seconde. Une attaque volumétrique est diluée et absorbée par les serveurs Edge à travers le monde avant d'atteindre le serveur d'origine.
- **Masquage de l'origine** : L'adresse IP réelle de votre serveur d'origine est masquée derrière les adresses IP publiques du CDN. L'attaquant ne peut cibler directement vos serveurs d'origine.

### Avantages et Limites
- **Avantages** :
  - Amélioration de la vitesse de chargement du site web pour les utilisateurs légitimes.
  - Capacité d'absorption des attaques volumétriques pratiquement illimitée.
- **Limites** :
  - Moins efficace pour protéger les requêtes dynamiques qui ne peuvent pas être mises en cache (ex: transactions bancaires, appels d'API complexes).

### Bonnes pratiques
1. Configurer le pare-feu du serveur d'origine pour qu'il n'accepte de connexions *que* depuis les plages d'adresses IP publiques officielles du CDN.
2. Mettre en cache le maximum de ressources statiques possibles.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
