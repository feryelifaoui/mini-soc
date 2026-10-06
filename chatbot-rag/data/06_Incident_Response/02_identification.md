# Identification de l'incident (Identification Phase)

## Introduction
Première étape technique de la réponse consistant à détecter et à qualifier officiellement une attaque DDoS en cours.

## Fiche Technique
| Signe observé | Diagnostic technique probable | Statut de l'incident |
| :--- | :--- | :--- |
| Ping normal, CPU serveur à 100% | Bug applicatif ou boucle de script | Incident Technique Interne |
| Ping > 1000ms, trafic entrant saturé | Attaque volumétrique (UDP Flood) | Incident de Sécurité (DDoS L4) |
| Ping normal, requêtes HTTP massives (RPS) | Attaque applicative (HTTP Flood) | Incident de Sécurité (DDoS L7) |

## Explications détaillées
### Principe et Fonctionnement
L'identification consiste à repérer un événement anormal et à confirmer qu'il s'agit bien d'une attaque de sécurité (un incident) et non d'une panne technique interne ou d'un pic de trafic légitime (faux positif). Face à un déni de service, l'équipe d'identification analyse les sondes réseau (NetFlow, SNMP), les temps de réponse des serveurs et les journaux système pour valider l'alerte.

### Processus de qualification DDoS
- **Étape 1 : Alerte initiale** : Le système de surveillance (Zabbix, Grafana) ou un utilisateur signale une indisponibilité.
- **Étape 2 : Vérification réseau** : L'ingénieur SOC examine la bande passante entrante (BPS) et le débit de paquets (PPS).
- **Étape 3 : Diagnostic de panne** : Exclure un problème de routage interne, un crash de disque dur sur le serveur, ou une erreur de configuration humaine récente.
- **Étape 4 : Déclaration formelle** : Si les métriques indiquent une surcharge externe inexpliquée avec des motifs de paquets répétitifs, l'incident DDoS est officiellement déclaré et la cellule de crise est activée.

### Bonnes pratiques
1. Définir des seuils d'alerte clairs (ex: Hausse du trafic entrant > 150% de la moyenne historique combinée avec une perte de paquets > 5%).
2. Utiliser un tableau de bord unifié dans le SOC pour corréler la bande passante réseau et le statut des applications web.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
