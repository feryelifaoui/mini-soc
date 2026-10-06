# SIEM (Security Information and Event Management)

## Introduction
Plateforme centralisée collectant, corrélant et analysant les événements de sécurité provenant de toute l'infrastructure de l'entreprise.

## Fiche Technique
| Fonctionnalité | Rôle dans la lutte contre le DDoS |
| :--- | :--- |
| **Agrégation** | Centralisation des logs pare-feu, WAF, DNS et serveurs |
| **Corrélation** | Liaison entre hausse de trafic réseau et indisponibilité applicative |
| **Tableaux de bord** | Visualisation de l'état de santé de l'infrastructure pendant la crise |
| **Exemples** | Splunk, Sentinel, QRadar, Elastic Security |

## Explications détaillées
### Principe et Fonctionnement
Le SIEM (Security Information and Event Management) collecte des millions de journaux d'événements (logs) provenant de diverses sources : pare-feux, serveurs web, annuaires Active Directory, IDS/IPS, routeurs, etc. Il normalise ces logs et applique des **règles de corrélation** en temps réel. Par exemple, si le SIEM détecte qu'un serveur web signale des erreurs HTTP 503 (logs du serveur) et que simultanément le pare-feu signale un pic d'adresses IP uniques sur le port 80 (logs réseau), il corrèle ces deux événements pour lever une alerte de niveau critique qualifiant une attaque DDoS en cours.

### Avantages et Limites
- **Avantages** :
  - Visibilité unifiée sur l'ensemble de la surface d'attaque.
  - Détection de scénarios d'attaque complexes (ex: DDoS utilisé comme diversion pour une exfiltration de données).
- **Limites** :
  - Coût d'acquisition et de licence souvent élevé (généralement basé sur le volume de données par jour).
  - Configuration et maintenance lourdes nécessitant des analystes spécialisés.

### Bonnes pratiques
1. Configurer des alertes prioritaires pour les métriques de disponibilité réseau.
2. Intégrer les flux de Threat Intelligence pour corréler les logs avec des listes d'adresses IP de botnets connus.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
