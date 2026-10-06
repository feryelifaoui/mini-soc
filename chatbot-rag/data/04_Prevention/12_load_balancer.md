# Répartiteur de charge (Load Balancer)

## Introduction
Équipement ou logiciel qui distribue le trafic réseau ou applicatif entrant sur un groupe de serveurs d'arrière-plan.

## Fiche Technique
| Algorithme | Mode de répartition | Comportement sous DDoS |
| :--- | :--- | :--- |
| **Round Robin** | Séquentiel strict | Distribue équitablement l'attaque sur tous les serveurs |
| **Least Connections**| Vers le serveur ayant le moins de sessions | Peut saturer rapidement les serveurs restants sains |
| **IP Hash** | Basé sur l'adresse IP du client | Dirige l'attaque d'une IP toujours vers le même serveur |

## Explications détaillées
### Principe et Fonctionnement
Un répartiteur de charge (Load Balancer) reçoit l'ensemble du trafic entrant destiné à un service et le distribue de manière équilibrée sur plusieurs serveurs d'arrière-plan (serveurs web ou applicatifs, appelés *pool* ou *farm*). La distribution peut se faire selon divers algorithmes : *Round Robin* (chacun son tour), *Least Connections* (vers le serveur le moins occupé) ou par hachage d'IP. Les répartiteurs de charge peuvent fonctionner au niveau de la couche 4 (TCP/UDP) ou de la couche 7 (HTTP/HTTPS, avec inspection du contenu).

### Rôle dans la prévention DDoS
- **Élimination du point de défaillance unique** : Distribue la charge d'une attaque HTTP Flood sur plusieurs serveurs web, évitant qu'un seul serveur ne s'effondre immédiatement.
- **Vérification de l'état de santé (Health Checks)** : Le Load Balancer surveille en permanence la réactivité de chaque serveur. Si un serveur commence à saturer et ne répond plus, le Load Balancer l'exclut temporairement du pool et redirige le trafic restant vers les serveurs sains.

### Avantages et Limites
- **Avantages** :
  - Scalabilité horizontale facilitée (on peut ajouter des serveurs au pool en temps réel pour absorber une hausse de trafic).
  - Gestion centralisée des certificats SSL/TLS et du filtrage initial.
- **Limites** :
  - Si le Load Balancer lui-même n'est pas configuré en cluster redondant, il devient la cible principale de l'attaque DDoS et le maillon faible de l'infrastructure.

### Bonnes pratiques
1. Déployer les Load Balancers en configuration active/passive avec synchronisation d'état en temps réel.
2. Utiliser HAProxy, F5 BIG-IP ou des répartiteurs de charge cloud managés (AWS ALB, Cloudflare).

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
