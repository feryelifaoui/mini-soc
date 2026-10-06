# Le cycle de réponse aux incidents (NIST / SANS)

## Introduction
Méthodologie standardisée décrivant les différentes étapes de gestion d'un incident de cybersécurité, de la préparation au retour d'expérience.

## Fiche Technique
| Phase du cycle | Objectif principal face au DDoS | Exemple d'action |
| :--- | :--- | :--- |
| **Préparation** | Anticiper et configurer les défenses | Configuration de SYN Cookies et scripts CLI |
| **Détection** | Qualifier et valider l'alerte | Analyse du volume de paquets par seconde (PPS) |
| **Confinement** | Limiter l'impact de la saturation | Activation de la déviation de routage BGP Anycast |
| **Récupération**| Rétablir la disponibilité nominale | Redémarrage progressif des serveurs web frontaux |
| **Post-Incident**| Améliorer le niveau de résilience | Analyse post-mortem et mise à jour des playbooks |

## Explications détaillées
### Principe et Fonctionnement
La réponse aux incidents (Incident Response - IR) s'appuie sur des cadres méthodologiques reconnus mondialement, principalement le modèle du **NIST** (National Institute of Standards and Technology - SP 800-61) et celui du **SANS Institute**. Ces modèles divisent la gestion d'un incident en un cycle continu de plusieurs phases distinctes, assurant une réaction méthodique, mesurée et efficace de la part de l'entreprise face à une crise telle qu'une attaque DDoS.

### Les phases du cycle (Modèle NIST)
1. **Préparation (Preparation)** : Établir la cellule de crise, configurer les outils de détection, former les équipes, et souscrire à des solutions de mitigation.
2. **Détection et Analyse (Detection & Analysis)** : Identifier les alertes, qualifier la nature de l'attaque DDoS (volumétrique, applicative) et analyser les indicateurs de compromission (IOCs).
3. **Confinement, Éradication et Récupération (Containment, Eradication & Recovery)** :
   - *Confinement* : Dérouter le trafic vers un centre de nettoyage ou appliquer des filtres temporaires.
   - *Éradication* : Éliminer la cause (ex. isoler les adresses de botnets, fermer les ports détournés).
   - *Récupération* : Rétablir le trafic normal, redémarrer les services affectés, et valider la réactivité de l'infrastructure.
4. **Activités Post-Incident (Post-Incident Activity / Lessons Learned)** : Rédiger le rapport d'incident, analyser l'efficacité de la réponse, et corriger les faiblesses identifiées pour renforcer la préparation future.

### Avantages et Limites
- **Avantages** :
  - Fournit un cadre clair évitant la panique et les décisions désordonnées pendant la crise.
  - Améliore continuellement la sécurité de l'entreprise grâce au retour d'expérience.
- **Limites** :
  - Nécessite une discipline stricte et un entraînement régulier pour être efficace en situation réelle.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
