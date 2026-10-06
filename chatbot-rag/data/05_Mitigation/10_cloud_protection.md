# Protection DDoS basée sur le Cloud (Cloud-Based Protection)

## Introduction
Utilisation d'infrastructures cloud mondiales de cybersécurité pour intercepter et nettoyer le trafic DDoS avant qu'il n'atteigne le réseau de l'entreprise.

## Fiche Technique
| Caractéristique | Protection On-Premise (Sur site) | Protection Cloud (Cloud-Based) |
| :--- | :--- | :--- |
| **Capacité d'absorption** | Limitée au débit physique de la liaison de l'entreprise | Pratiquement illimitée (Échelle mondiale) |
| **Mitigation volumétrique**| Faible (les tuyaux saturent avant le pare-feu) | Excellente (filtrage en amont) |
| **Gestion** | Interne (équipes réseau de l'entreprise) | Externalisée / Gérée par le fournisseur cloud |

## Explications détaillées
### Principe et Fonctionnement
La protection DDoS dans le cloud consiste à déporter la sécurité périmétrique de l'entreprise vers des fournisseurs cloud spécialisés (ex: Cloudflare, Akamai, AWS Shield, Azure DDoS Protection). Ces prestataires disposent de réseaux mondiaux massifs d'infrastructures Anycast et de multiples centres de nettoyage. L'entreprise modifie sa configuration DNS ou ses annonces de routage BGP pour faire converger tout le trafic internet mondial vers le cloud du prestataire. Le trafic y est inspecté, nettoyé en temps réel, et seul le flux purifié est acheminé vers les serveurs réels de l'entreprise via des tunnels privés ou cryptés (GRE, IPsec).

### Rôle dans la mitigation DDoS
C'est la solution ultime contre les attaques volumétriques modernes :
- **Bande passante élastique** : Capacité à absorber des attaques de niveau térabit (ex: 3.4 Tbps) qu'aucun datacenter d'entreprise classique ne pourrait physiquement raccorder.
- **Threat Intelligence globale** : Le cloud de protection, surveillant le trafic de millions de sites web, identifie instantanément les nouvelles adresses IP de bots d'attaque et bloque la menace sur l'ensemble de ses clients simultanément.

### Avantages et Limites
- **Avantages** :
  - Sécurité et disponibilité garanties par des contrats d'engagements (SLA) stricts.
  - Décharge complète de la gestion réseau et de la surcharge CPU liée à l'inspection.
- **Limites** :
  - Dépendance vis-à-vis d'un tiers pour la connectivité et la sécurité de l'entreprise.
  - Coûts récurrents (abonnements mensuels).

### Bonnes pratiques
1. Restreindre totalement les accès physiques et logiques de votre serveur d'origine : aucun accès internet direct ne doit être possible en dehors de la liaison sécurisée avec le cloud de protection (pour éviter le contournement de protection - Origin Bypass).
2. Intégrer les métriques du cloud protecteur dans le SIEM interne de l'entreprise.

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
