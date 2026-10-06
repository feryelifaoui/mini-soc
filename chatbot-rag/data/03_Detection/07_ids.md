# IDS (Intrusion Detection System)

## Introduction
Système passif de détection d'intrusions qui surveille le trafic réseau et génère des alertes en cas d'activité suspecte ou malveillante.

## Fiche Technique
| Critère | Description |
| :--- | :--- |
| **Mode de connexion** | Hors ligne (Out-of-band / TAP / SPAN) |
| **Action** | Alerte uniquement (Log, Email, Alert SIEM) |
| **Risque réseau** | Nul (pas de point de défaillance unique) |
| **Exemples** | Snort, Suricata, Zeek |

## Explications détaillées
### Principe et Fonctionnement
Un IDS (Intrusion Detection System) analyse le trafic réseau de manière passive (souvent connecté à un port miroir - SPAN port - d'un commutateur). Il examine les paquets pour y détecter des signatures d'attaques ou des anomalies comportementales. S'il identifie un comportement suspect (ex: un scan de ports Nmap ou le début d'un SYN Flood), l'IDS génère une alerte dans une console d'administration ou envoie un log au SIEM. **L'IDS ne bloque pas le trafic lui-même** ; il a un rôle purement informatif et d'alerte pour les équipes de sécurité.

### Avantages et Limites
- **Avantages** :
  - Aucun impact sur le flux de trafic légitime (pas de risque de coupure réseau en cas de dysfonctionnement de l'IDS).
  - Facile à déployer en parallèle de l'infrastructure existante.
- **Limites** :
  - N'arrête pas l'attaque en cours de manière autonome.
  - Génère des alertes qui doivent être analysées par un humain (fatigue des alertes si mal configuré).

### Bonnes pratiques
1. Configurer des règles d'alerte ciblées pour éviter la saturation de la console d'administration.
2. Placer l'IDS derrière le pare-feu externe pour n'analyser que le trafic ayant franchi les premières lignes de défense.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
