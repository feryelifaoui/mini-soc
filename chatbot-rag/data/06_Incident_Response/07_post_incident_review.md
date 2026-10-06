# Retour d'expérience (Lessons Learned / Post-Incident Activity)

## Introduction
Analyse critique post-crise visant à identifier les forces et les faiblesses de la réponse apportée et à améliorer la sécurité globale.

## Fiche Technique
| Point fort observé | Point faible identifié | Action corrective décidée |
| :--- | :--- | :--- |
| Le WAF a bloqué 90% des requêtes | Latence de détection réseau de 20 minutes | Configurer des sondes NetFlow en temps réel |
| Collaboration étroite avec le FAI | La page de statut externe a planté | Héberger la page de statut chez un hébergeur tiers indépendant |
| Les serveurs ont résisté | La base de données a été saturée | Implémenter un coupe-circuit (Circuit Breaker) |

## Explications détaillées
### Principe et Fonctionnement
La phase de retour d'expérience (souvent appelée "Lessons Learned" ou réunion post-mortem) est l'étape la plus importante à long terme du cycle de réponse. Elle réunit l'ensemble des acteurs de la cellule de crise (SOC, réseau, système, communication, direction générale) pour analyser froidement le déroulement de l'incident. L'objectif n'est pas de chercher des coupables, mais de comprendre ce qui a bien fonctionné, ce qui a échoué (ex: retards de communication, mauvais outils de détection) et de définir un plan d'action pour renforcer l'infrastructure.

### Questions clés lors du retour d'expérience
- Quel a été le vecteur d'attaque précis ? Quelle a été sa durée et son impact financier réel ?
- Les outils de détection ont-ils fonctionné rapidement ? Dans quel délai l'alerte a-t-elle été escaladée ?
- Les playbooks de réponse aux incidents étaient-ils à jour et applicables ?
- La communication interne et externe (avec les clients, les FAI, le public) a-t-elle été bien gérée ?
- Quelles modifications d'architecture technique ou organisationnelle doivent être apportées pour résister à une attaque similaire ?

### Bonnes pratiques
1. Organiser la réunion post-mortem dans les 7 jours ouvrés suivant la clôture de l'incident (pendant que les détails techniques sont encore frais dans les mémoires).
2. Rédiger un document de synthèse officiel ("Rapport Post-Mortem") contenant le plan d'action correctif avec des responsables désignés et des dates d'échéance.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
