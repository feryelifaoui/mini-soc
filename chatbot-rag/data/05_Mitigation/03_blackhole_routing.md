# Routage Trou Noir (Blackhole Routing / Null Routing)

## Introduction
Technique de mitigation réseau de dernier recours consistant à rediriger tout le trafic destiné à une adresse IP ciblée vers une interface virtuelle nulle.

## Fiche Technique
| Type de routage | Trafic légitime | Trafic d'attaque | Impact sur la victime |
| :--- | :--- | :--- | :--- |
| **Normal** | Autorisé | Autorisé (Sature) | Ralentissement ou Crash |
| **Blackhole** | Détruit | Détruit | Totalement inaccessible |

## Explications détaillées
### Principe et Fonctionnement
Le routage trou noir (Blackhole Routing ou Null Routing) consiste à modifier la table de routage d'un routeur (souvent chez le fournisseur d'accès internet en amont) pour envoyer tous les paquets destinés à l'adresse IP de la victime vers une interface virtuelle nulle (ex: `/dev/null` ou `Null0`). Les paquets sont alors détruits instantanément au niveau matériel, sans traitement CPU et sans générer de réponse ICMP.
Cette action est généralement propagée via BGP en utilisant une communauté spécifique (BGP Blackhole Community).

### Rôle dans la mitigation DDoS
Le Blackholing est une mesure d'autodéfense réseau extrême :
- **Protection de l'infrastructure** : Il évite que l'attaque DDoS volumétrique ne sature complètement le lien d'accès internet global du FAI ou du datacenter, ce qui paralyserait l'ensemble des autres clients hébergés sur le même réseau.
- **Sacrifice de la cible** : Pour sauver la connectivité globale du réseau, on accepte de rendre la machine ciblée (la victime) totalement inaccessible de l'extérieur.

### Avantages et Limites
- **Avantages** :
  - Arrêt immédiat de la saturation réseau sur les liens de transit.
  - Simple et rapide à propager au niveau mondial via BGP.
- **Limites** :
  - L'attaquant atteint son objectif initial : le service visé est indisponible (déni de service complet, auto-infligé).

### Bonnes pratiques
1. Configurer le blackholing de manière automatisée uniquement sur des adresses IP secondaires ou des machines non critiques.
2. Utiliser le "Remote Triggered Black Hole" (RTBH) pour une réaction rapide en amont chez le FAI.

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
