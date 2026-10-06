# Architecture résiliente (Resilient Architecture)

## Introduction
Modèle de conception d'infrastructure capable de subir des perturbations majeures tout en maintenant un niveau de service acceptable.

## Fiche Technique
| Concept de conception | Rôle défensif DDoS | Exemple d'application |
| :--- | :--- | :--- |
| **Auto-scaling** | Absorption élastique de la charge | Ajout de conteneurs Kubernetes |
| **Circuit Breaker** | Protection des dépendances backend | Isolation de la base de données saturée |
| **Graceful Degradation**| Maintien d'un service minimal | Affichage d'une page HTML statique |

## Explications détaillées
### Principe et Fonctionnement
La résilience va au-delà de la haute disponibilité. Alors que la haute disponibilité cherche à empêcher toute panne, la résilience accepte la possibilité que des pannes ou des surcharges massives surviennent, et se concentre sur la capacité du système à continuer de fonctionner en mode dégradé (Graceful Degradation) et à récupérer rapidement sa capacité nominale une fois la crise passée.

### Concepts clés de l'architecture résiliente face au DDoS
- **Coupe-circuits (Circuit Breakers)** : Si un service interne non critique (ex. le moteur de recommandation de produits sur un e-commerce) est saturé, le système coupe temporairement son alimentation ou son appel pour préserver le fonctionnement des services vitaux (le panier d'achat et le paiement).
- **Auto-scaling (Mise à l'échelle automatique)** : Capacité de l'infrastructure cloud à créer dynamiquement de nouveaux serveurs virtuels en quelques minutes en réponse à une hausse soudaine du trafic réseau ou du CPU.
- **Dégradation gracieuse** : Proposer aux utilisateurs une version statique simplifiée du site web ou une page d'attente polie si les serveurs applicatifs backend sont temporairement indisponibles.

### Avantages et Limites
- **Avantages** :
  - Survie de l'application même sous une charge d'attaque extrême.
  - Rétablissement automatique sans intervention humaine obligatoire.
- **Limites** :
  - Nécessite une refonte applicative importante au niveau du code logiciel, pas seulement au niveau réseau.

### Bonnes pratiques
1. Concevoir des applications basées sur des microservices découplés plutôt qu'un unique bloc monolithique.
2. Utiliser des files d'attente de messages (ex: RabbitMQ, Kafka) pour lisser les pics de requêtes d'écriture.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
