# Centre de nettoyage (Scrubbing Center)

## Introduction
Infrastructure de sécurité centralisée et hautement performante dédiée au nettoyage des flux de données pollués par les attaques DDoS.

## Fiche Technique
| Critère | Scrubbing Center permanent (Always-On) | Scrubbing Center à la demande (On-Demand) |
| :--- | :--- | :--- |
| **Latence nominale** | Légère latence permanente (5-10ms) | Aucune latence hors attaque |
| **Temps de réaction** | Instantané | 3 à 10 minutes (propagation BGP) |
| **Coût** | Très élevé | Modéré (facturation à l'usage) |

## Explications détaillées
### Principe et Fonctionnement
Un centre de nettoyage (Scrubbing Center) est une infrastructure physique implantée au cœur des réseaux des grands opérateurs télécoms ou des fournisseurs de cybersécurité cloud. Il dispose d'une bande passante gigantesque (plusieurs térabits par seconde) et abrite des baies d'équipements de sécurité matériels spécialisés (tels que des appliances de détection et de mitigation DDoS, des pare-feux applicatifs et des répartiteurs de charge). En situation de crise, tout le trafic mondial destiné à la victime est redirigé vers ce centre pour y être purifié.

### Rôle dans la mitigation DDoS
- **Absorption volumétrique** : La capacité réseau du centre lui permet d'absorber les attaques géantes (plusieurs centaines de Gbps) que le lien internet classique d'une entreprise ne pourrait pas supporter.
- **Mutualisation des défenses** : Permet aux entreprises de bénéficier d'outils de sécurité ultra-performants et onéreux sous forme d'abonnement.

### Avantages et Limites
- **Avantages** :
  - Protection contre les attaques de niveau national ou mondial.
  - Équipes d'ingénieurs spécialisés (SOC) gérant le matériel en permanence.
- **Limites** :
  - Temps d'activation (quelques minutes sont parfois nécessaires pour propager les modifications de routage BGP lors d'une redirection non permanente).

### Bonnes pratiques
1. Choisir un prestataire de centre de nettoyage disposant de multiples points de présence (PoPs) à l'international pour réduire la latence.
2. Tester régulièrement la procédure d'activation (par exemple lors de fenêtres de maintenance nocturnes).

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
