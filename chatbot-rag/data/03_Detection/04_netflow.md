# NetFlow

## Introduction
Protocole réseau développé par Cisco permettant de collecter des informations sur les flux IP traversant les routeurs et commutateurs.

## Fiche Technique
| Paramètre | Description |
| :--- | :--- |
| **Développeur** | Cisco (standardisé via IPFIX) |
| **Ports typiques** | UDP 2055, 9995 |
| **Niveau d'analyse** | Couches 3 et 4 |
| **Usage DDoS** | Détection d'attaques volumétriques et de réflexion |

## Explications détaillées
### Principe et Fonctionnement
NetFlow fonctionne en regroupant les paquets réseau individuels en "flux" (flows) partageant 7 clés caractéristiques : IP source, IP destination, Port source, Port destination, Protocole (L4), Type de service (ToS) et Interface d'entrée. Au lieu d'analyser chaque paquet physique (très lourd), le routeur envoie des résumés de flux (métadonnées) à un outil centralisé appelé **NetFlow Collector**. Ces informations permettent d'analyser le trafic réseau global, d'identifier les goulets d'étranglement et de détecter les anomalies de trafic (comme un volume anormal de paquets UDP provenant d'une région géographique spécifique).

### Avantages et Limites
- **Avantages** :
  - Faible impact sur les performances des équipements réseau (par rapport à la capture de paquets complète).
  - Visibilité globale sur l'ensemble de l'infrastructure réseau.
- **Limites** :
  - Pas d'inspection du contenu des paquets (Payload), uniquement les en-têtes de couches 3/4.
  - Le traitement s'effectue souvent de manière asynchrone (léger retard de quelques minutes dans la réception des flux).

### Bonnes pratiques
1. Configurer NetFlow sur tous les routeurs frontières de l'entreprise.
2. Utiliser un collecteur NetFlow doté de capacités d'analyse de sécurité en temps réel.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
