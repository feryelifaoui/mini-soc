# Métriques réseau clés pour le DDoS

## Introduction
Les indicateurs quantitatifs mesurables servant à évaluer la force d'une attaque et l'état de l'infrastructure.

## Fiche Technique
| Métrique | Unité de mesure | Cible de saturation principale | Type d'attaque type |
| :--- | :--- | :--- | :--- |
| **BPS** | Gbps / Tbps | Liens réseau FAI, Interfaces physiques | UDP Flood, Amplification NTP |
| **PPS** | Mpps (Millions de PPS)| Processeur routeur, Table d'états pare-feu | SYN Flood, ACK Flood |
| **RPS** | RPS / QPS | Pool de connexions Web, Serveur Application | HTTP Flood, Slowloris |

## Explications détaillées
### Principe et Fonctionnement
Lors de la surveillance réseau et de l'analyse d'incident, plusieurs métriques quantitatives spécifiques doivent être observées de près pour évaluer l'intensité de l'attaque et l'efficacité des mesures d'atténuation.

### Les 4 métriques fondamentales
- **Bande passante (BPS - Bits Per Second)** : Mesure le volume physique de données entrant dans le réseau. Exprimé en Gbps ou Tbps pour les attaques volumétriques. Indique le niveau de saturation des liens physiques.
- **Débit de paquets (PPS - Packets Per Second)** : Mesure le nombre de paquets de données traités par seconde par les commutateurs et pare-feux. Une attaque avec de très petits paquets (ex: SYN de 40 octets) peut générer un faible débit en Gbps mais un nombre de PPS gigantesque (ex: 20 millions de PPS), saturant les processeurs réseau.
- **Débit de requêtes (RPS - Requests Per Second)** : Métrique de couche 7 mesurant le nombre de requêtes HTTP/HTTPS reçues par seconde par le serveur web ou le WAF.
- **Requêtes par seconde DNS (QPS - Queries Per Second)** : Mesure le nombre de requêtes de résolution DNS reçues par seconde par les serveurs DNS.

### Bonnes pratiques
1. S'assurer que vos outils de métriques ont une résolution temporelle fine (ex: échantillonnage à la seconde plutôt qu'à la minute) pour capter les attaques flash.
2. Analyser conjointement le ratio PPS/BPS pour identifier les caractéristiques physiques des paquets d'attaque.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
