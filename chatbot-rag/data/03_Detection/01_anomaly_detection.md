# Détection d'anomalies (Anomaly Detection)

## Introduction
Méthode de détection basée sur l'identification d'écarts par rapport à un profil de comportement réseau normal préalablement établi.

## Fiche Technique
| Caractéristique | Détail |
| :--- | :--- |
| **Méthode** | Modélisation comportementale (Baseline) |
| **Cible** | Attaques volumétriques, protocolaires et applicatives |
| **Taux de faux positifs** | Moyen à Élevé |
| **Détection Zero-Day** | Excellente |

## Explications détaillées
### Principe et Fonctionnement
La détection d'anomalies repose sur le concept de ligne de base (*baseline*). Le système analyse le trafic réseau normal pendant une période d'apprentissage (ex: 2 semaines) pour modéliser les schémas d'activité habituels (volume de trafic par heure, types de protocoles, répartition géographique, etc.). Une fois la ligne de base établie, le système surveille le trafic en temps réel. Si une métrique s'écarte de manière significative de la normale (ex: pic de trafic UDP de +400% un dimanche soir), le système déclenche une alerte ou active des règles de filtrage.

### Avantages et Limites
- **Avantages** :
  - Capable de détecter des attaques inconnues ou de type "Zero-Day" (pour lesquelles aucune signature n'existe).
  - S'adapte à l'évolution naturelle du trafic réseau de l'entreprise.
- **Limites** :
  - Risque élevé de faux positifs lors d'événements business légitimes (soldes, campagne marketing massive, mise à jour logicielle globale).
  - Phase d'apprentissage initiale vulnérable : si une attaque lente se produit pendant l'apprentissage, elle sera intégrée dans la baseline comme du trafic normal.

### Bonnes pratiques
1. Mettre à jour régulièrement la ligne de base pour refléter les changements d'infrastructure.
2. Combiner la détection d'anomalies avec la détection par signatures pour affiner la précision.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
