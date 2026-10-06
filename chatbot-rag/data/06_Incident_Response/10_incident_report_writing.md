# Rédaction d'un rapport d'incident DDoS

## Introduction
Guide méthodologique pour rédiger le rapport officiel post-incident destiné à la direction générale, aux clients et aux autorités de régulation.

## Fiche Technique
| Section du rapport | Destinataire principal | Niveau de détail technique |
| :--- | :--- | :--- |
| **Executive Summary** | Comité de direction (C-Level) | Faible (orienté impact business) |
| **Timeline / Investigation**| Équipe Sécurité, SOC | Très élevé (Commandes, Logs, Ports) |
| **Action Plan** | Équipe IT / Management | Moyen (Projets, Budgets, Échéances) |

## Explications détaillées
### Principe et Fonctionnement
Le rapport d'incident (ou rapport d'analyse post-mortem) documente l'ensemble de l'événement de manière objective. Il constitue la trace historique officielle de la crise et sert de base légale ou contractuelle (ex: pour l'assurance ou pour justifier le respect des SLAs).

### Structure type d'un rapport d'incident DDoS
1. **Synthèse administrative (Executive Summary)** : Résumé non technique décrivant la date, la durée, l'impact business global et la résolution de l'incident. Destiné aux décideurs.
2. **Chronologie détaillée des événements (Timeline)** : Historique minute par minute de la crise (première alerte, qualification, détection des vecteurs, actions de mitigation appliquées, retour au fonctionnement nominal).
3. **Analyse technique détaillée** : Vecteurs d'attaque précis, volume (Gbps, PPS, RPS), adresses IP sources prédominantes, cibles internes visées, signatures identifiées.
4. **Impact business et financier** : Temps total d'indisponibilité des services, dysfonctionnements constatés, perte d'exploitation estimée.
5. **Plan d'action correctif (Post-Mortem Actions)** : Liste des mesures techniques et organisationnelles décidées pour éviter qu'un incident similaire ne se reproduise, avec responsables et échéances.

### Bonnes pratiques
1. Être précis dans l'horodatage des faits (utiliser l'heure UTC de manière constante pour corréler les logs réseau et système).
2. Annexer au rapport les graphiques de monitoring réseau pertinents (ex: pic de trafic sFlow ou NetFlow).
3. Rédiger le rapport sous forme de document PDF sécurisé, classé confidentiel et stocké dans l'outil de gestion documentaire de l'entreprise.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
