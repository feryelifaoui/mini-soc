# Listes blanches (Whitelisting)

## Introduction
Stratégie de sécurité stricte consistant à bloquer tout trafic par défaut et à n'autoriser que les sources explicitement approuvées.

## Fiche Technique
| Cas d'usage adapté | Cas d'usage inadapté |
| :--- | :--- |
| Flux d'API inter-entreprises (B2B) avec IP fixes | Site e-commerce grand public |
| Accès d'administration système (SSH/RDP) | Application mobile tout public |
| Réplication de bases de données | Résolution DNS publique |

## Explications détaillées
### Principe et Fonctionnement
La liste blanche (Whitelisting) applique une approche "Zéro Trust" : tout le trafic est bloqué à moins qu'il ne provienne d'une entité explicitement déclarée comme sûre. Par exemple, une entreprise peut configurer son pare-feu externe pour n'accepter de connexions SSH ou VPN que depuis les adresses IP fixes de ses employés ou de ses partenaires commerciaux autorisés.

### Rôle dans la prévention DDoS
- **Immunité totale** : Un serveur ou une API interne protégé par une liste blanche est totalement immunisé contre les attaques DDoS provenant d'Internet, car tout paquet provenant d'une IP non listée est jeté instantanément.
- **Protection des accès administratifs** : Sécuriser les consoles de gestion (ex. interfaces réseau des routeurs) contre toute inondation de requêtes.

### Avantages et Limites
- **Avantages** :
  - Niveau de sécurité le plus élevé possible.
  - Élimination complète des vecteurs d'attaque externes non autorisés.
- **Limites** :
  - Inapplicable pour les sites web publics ou les services grand public (ex. e-commerce) où n'importe quel internaute mondial doit pouvoir se connecter librement.
  - Surcharge administrative importante pour gérer les changements d'adresses IP des utilisateurs légitimes.

### Bonnes pratiques
1. Utiliser le whitelisting pour tous les flux d'administration système (SSH, RDP, bases de données).
2. Mettre en place un portail d'authentification préalable ou un VPN pour intégrer dynamiquement des IP dans la liste blanche.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
