# Routage Sinkhole (Sinkhole Routing)

## Introduction
Redirection du trafic d'attaque vers un sous-réseau spécifique et isolé à des fins d'analyse, d'inspection et de blocage sélectif.

## Fiche Technique
| Critère | Blackhole Routing | Sinkhole Routing |
| :--- | :--- | :--- |
| **Action sur le paquet** | Destruction immédiate (Drop) | Redirection vers un réseau d'analyse |
| **Objectif** | Protéger le réseau global de la saturation | Inspecter le trafic et filtrer |
| **Disponibilité service**| Nulle (site coupé) | Partielle (selon efficacité du filtrage) |

## Explications détaillées
### Principe et Fonctionnement
Contrairement au routage trou noir qui détruit tout le trafic, le routage Sinkhole (ou "puit d'égout") redirige le trafic suspect destiné à la victime vers un réseau fermé et isolé de l'infrastructure principale. Ce réseau contient des serveurs d'analyse équipés de sniffeurs de paquets, d'IDS/IPS et de consoles de surveillance. L'objectif est d'analyser la structure exacte de l'attaque, d'identifier les signatures et les adresses IP des bots pour ensuite appliquer des règles de filtrage chirurgicales, tout en essayant de sauver le trafic légitime.

### Rôle dans la mitigation DDoS
- **Investigation criminelle et technique** : Capturer les paquets d'attaque pour en comprendre le fonctionnement et identifier le botnet.
- **Filtrage intelligent** : Permet de concevoir des politiques de nettoyage dynamiques avant de réadmettre le trafic sain dans le réseau de production.

### Avantages et Limites
- **Avantages** :
  - Permet de comprendre l'attaque en détail (reverse-engineering des paquets).
  - Évite la coupure totale induite par le Blackholing.
- **Limites** :
  - Nécessite une infrastructure d'analyse robuste et sécurisée capable de supporter de hauts débits.

### Bonnes pratiques
1. Isoler physiquement ou logiquement le réseau Sinkhole du reste du système d'information de l'entreprise.
2. Automatiser la capture réseau (fichiers PCAP) dès qu'un flux est dérouté vers le Sinkhole.

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
