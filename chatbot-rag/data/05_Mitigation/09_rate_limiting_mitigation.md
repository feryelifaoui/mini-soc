# Limitation du débit en mitigation (Mitigation Rate Limiting)

## Introduction
Application dynamique de limites de débit de trafic réseau et applicatif pour préserver les ressources d'infrastructure pendant une attaque.

## Fiche Technique
| Niveau d'application | Protocole visé | Objectif défensif | Impact utilisateur légitime |
| :--- | :--- | :--- | :--- |
| **Réseau (L3/L4)** | UDP, ICMP, TCP SYN | Limiter la bande passante globale | Aucun (si les services sont HTTP) |
| **Applicatif (L7)** | HTTP GET/POST | Protéger le processeur du backend | Rejet temporaire de requêtes (429) |

## Explications détaillées
### Principe et Fonctionnement
Alors que le Rate Limiting préventif s'applique en permanence à faible niveau, la limitation de débit en phase de mitigation est activée de manière agressive pendant une attaque. Elle consiste à brider le trafic sur des protocoles ou des ports spécifiques pour éviter la panne générale. Par exemple, si le serveur web subit un HTTP Flood, le système de mitigation peut réduire temporairement le quota de requêtes autorisées pour les utilisateurs non authentifiés, tout en préservant le débit normal pour les utilisateurs ayant une session active (session cookies valides).

### Rôle dans la mitigation DDoS
- **Lissage du trafic** : Réduire le volume entrant sous le seuil maximal de capacité du serveur.
- **Priorisation de flux** : Accorder la priorité de traitement au trafic le plus important (ex. requêtes de paiement) au détriment du trafic d'information général.

### Avantages et Limites
- **Avantages** :
  - Évite le crash complet du serveur web ou de la base de données.
  - Facile à activer d'urgence sur un WAF ou un répartiteur de charge.
- **Limites** :
  - Entraîne le rejet d'une partie des requêtes d'utilisateurs légitimes non authentifiés, créant un déni de service partiel.

### Bonnes pratiques
1. Mettre en place des pages de retour HTTP conviviales (ex. "Serveur temporairement surchargé, veuillez patienter") pour les requêtes rejetées.
2. Configurer la limitation de débit au niveau du proxy inverse frontal pour économiser les serveurs backend.

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
