# Surveillance réseau (Network Monitoring)

## Introduction
Surveillance continue de la santé, des performances et de la disponibilité des équipements et liaisons réseau.

## Fiche Technique
| Outil type | Métrique surveillée | Protocole de collecte |
| :--- | :--- | :--- |
| **Zabbix / PRTG** | Bande passante de l'interface, État du port | SNMP |
| **Prometheus** | CPU, RAM, Nombre de threads actifs | HTTP Exporter / Node Exporter |
| **Ping** | Latence, Perte de paquets (Packet loss) | ICMP |

## Explications détaillées
### Principe et Fonctionnement
La surveillance réseau (ou Network Monitoring) s'appuie sur des protocoles comme **SNMP** (Simple Network Management Protocol) ou ICMP pour interroger régulièrement les équipements d'infrastructure (routeurs, commutateurs, serveurs). Elle permet de suivre des indicateurs physiques tels que l'utilisation de la bande passante sur un port de switch, la charge CPU d'un pare-feu, ou la perte de paquets sur une liaison de transit. En cas de dépassement de seuil prédéfini (ex: CPU pare-feu > 90% pendant plus de 2 minutes), le système envoie une alerte immédiate aux équipes réseau.

### Avantages et Limites
- **Avantages** :
  - Outils souvent simples à configurer et indispensables au quotidien (NMS - Network Management System).
  - Permet d'identifier instantanément quel équipement physique sature lors d'une attaque.
- **Limites** :
  - Ne donne pas d'informations sur le contenu ou l'origine du trafic, uniquement sur les performances globales.

### Bonnes pratiques
1. Configurer des alertes avec des seuils de pré-alerte (ex. 75% d'utilisation) pour anticiper la saturation complète.
2. Utiliser des outils d'affichage graphique en temps réel (ex: Grafana) installés sur des écrans du SOC.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
