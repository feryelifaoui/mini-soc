# Éradication de l'attaque (Eradication Phase)

## Introduction
Élimination complète des vecteurs d'attaque, des composants malveillants et des vulnérabilités exploitées.

## Fiche Technique
| Cible de l'éradication | Action technique | Objectif à long terme |
| :--- | :--- | :--- |
| **Vecteurs de protocoles** | Désactivation des fonctions obsolètes (monlist, etc.) | Empêcher le détournement futur |
| **Adresses IP des Bots** | Intégration dans des listes de réputation | Filtrage automatique au périmètre |
| **Failles de l'OS** | Application des mises à jour de sécurité (Patches) | Éviter les plantages système (DoS) |

## Explications détaillées
### Principe et Fonctionnement
Dans le cadre d'une cyberattaque classique (ex: malware ou intrusion), l'éradication consiste à supprimer le code malveillant des machines infectées. Face à un DDoS (attaque externe), l'éradication prend une autre forme : elle consiste à s'assurer que l'attaque est totalement étouffée, que les sources malveillantes sont bloquées, et que les failles ou faiblesses d'infrastructure exploitées (ex: serveurs NTP internes mal configurés participant à l'attaque) sont corrigées.

### Actions clés d'éradication DDoS
1. **Nettoyage des listes d'IP** : Consolider les listes d'adresses IP attaquantes identifiées et les intégrer durablement dans les politiques de blocage (Threat Intelligence).
2. **Durcissement des configurations (Hardening)** : Corriger définitivement les configurations système fragiles (ex: désactiver UPnP sur les routeurs, appliquer les patchs de sécurité de la pile réseau de l'OS).
3. **Collaboration avec les autorités et FAI** : Signaler les serveurs de Command & Control (C2) et les bots identifiés aux fournisseurs d'accès internet et aux cellules d'urgence cyber (CERT/CSIRT) pour démanteler le botnet à la source.

### Bonnes pratiques
1. Documenter toutes les adresses IP et signatures d'attaque identifiées pendant l'incident pour enrichir vos bases de données locales.
2. Ne pas supprimer les règles de confinement trop rapidement : s'assurer que l'attaque a définitivement cessé avant de relâcher les défenses.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
