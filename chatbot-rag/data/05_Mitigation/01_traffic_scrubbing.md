# Nettoyage du trafic (Traffic Scrubbing)

## Introduction
Processus actif consistant à analyser le trafic entrant et à séparer en temps réel le trafic malveillant (DDoS) du trafic légitime.

## Fiche Technique
| Étape du processus | Description technique | Action associée |
| :--- | :--- | :--- |
| **1. Détection** | Dépassement des seuils nominaux de trafic | Alerte SNMP / NetFlow |
| **2. Redirection** | Déroutement du trafic vers le système de nettoyage | Modification BGP ou DNS |
| **3. Filtrage** | Inspection et séparation du trafic (Scrubbing) | Drop / Rate Limit / Challenge |
| **4. Livraison** | Transmission du trafic propre à l'origine | Tunnel GRE / Proxy inverse |

## Explications détaillées
### Principe et Fonctionnement
Le nettoyage du trafic (Traffic Scrubbing) consiste à faire transiter l'ensemble des paquets réseau destinés à l'entreprise cible à travers un équipement ou un service d'analyse de sécurité intermédiaire. Ce système utilise des algorithmes d'analyse comportementale, de corrélation de protocoles et de filtrage par signatures pour identifier les anomalies. Le trafic identifié comme d'attaque (ex: paquets UDP usurpés ou requêtes HTTP répétitives de bots) est jeté (*dropped*), tandis que le trafic légitime (ex: requêtes de clients réels) est transmis proprement au serveur d'origine.

### Rôle dans la mitigation DDoS
- **Filtrage en ligne (In-line Filtering)** : Assure la continuité de l'activité commerciale en ne bloquant que l'attaque.
- **Séparation de flux** : Évite d'appliquer des blocages globaux (comme le Null Routing) qui pénalisent les vrais clients.

### Avantages et Limites
- **Avantages** :
  - Maintien opérationnel du site web ou de l'application pendant la crise.
  - Taux élevé de détection des attaques sophistiquées (Couches 3, 4 et 7).
- **Limites** :
  - Peut induire une légère latence réseau supplémentaire (quelques millisecondes) due au déroutement et à l'inspection.
  - Coût financier élevé des équipements physiques de nettoyage ou du service cloud associé.

### Bonnes pratiques
1. Configurer le système pour qu'il s'active automatiquement en cas de détection de dépassement de seuil de trafic.
2. S'assurer que le lien réseau de retour (du centre de nettoyage vers l'entreprise) est sécurisé et crypté (ex: via tunnel GRE).

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
