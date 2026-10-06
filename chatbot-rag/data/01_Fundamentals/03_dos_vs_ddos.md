# Différences DoS vs DDoS

## Introduction
Bien que les termes DoS (Denial of Service) et DDoS (Distributed Denial of Service) décrivent tous deux une interruption de service, ils diffèrent radicalement dans leur exécution, leur échelle et les méthodes requises pour les combattre. Comprendre ces différences est crucial pour concevoir une stratégie de défense adaptée.

## Explications détaillées
La différence fondamentale réside dans le nombre de sources d'attaque. Un DoS provient d'un point unique, tandis qu'un DDoS provient de sources multiples réparties dans le monde entier.

### Analyse comparative des mécanismes

#### 1. Architecture de l'attaque
- **DoS** : Relation de 1 à 1. Une machine attaquante cible directement une machine victime. Le flux de données est rectiligne.
- **DDoS** : Relation de N à 1. Des milliers de machines attaquantes (le Botnet) ciblent simultanément une seule victime. L'attaque est coordonnée via un serveur de commande (C2).

#### 2. Volume et puissance
- **DoS** : Limité par la bande passante montante de la machine de l'attaquant (généralement moins de 1 Gbps).
- **DDoS** : Pratiquement illimité. En combinant la bande passante de milliers de connexions, les attaques DDoS dépassent régulièrement les 500 Gbps et peuvent atteindre plusieurs Tbps.

#### 3. Complexité de la détection et du filtrage
- **DoS** : Simple. Les pare-feux détectent un volume anormal provenant d'une seule adresse IP et appliquent une règle de blocage (Null Routing ou ACL).
- **DDoS** : Très difficile. Le trafic provient de milliers d'adresses IP légitimes (ordinateurs d'utilisateurs infectés). Bloquer ces adresses une par une est inefficace et risque de bloquer de vrais utilisateurs (faux positifs).

## Tableau comparatif : DoS vs DDoS
| Critère | DoS (Denial of Service) | DDoS (Distributed Denial of Service) |
| :--- | :--- | :--- |
| **Nombre de sources** | Une seule adresse IP / machine | Des milliers à des millions d'IP |
| **Origine du trafic** | Ciblée et identifiable | Globale et dispersée |
| **Volume de l'attaque** | Faible à modéré (< 1 Gbps) | Très élevé (jusqu'à plusieurs Tbps) |
| **Coût de mise en œuvre** | Pratiquement nul | Moyen à élevé (location/création de botnet) |
| **Technique de défense principale** | ACL Pare-feu, blocage d'IP simple | Scrubbing Cloud, Réseau Anycast, BGP Flowspec |
| **Complexité d'atténuation** | Faible | Très élevée |

## Cas d'utilisation typiques
- **DoS** : Souvent utilisé par des attaquants amateurs (script kiddies) ciblant des serveurs de jeux personnels ou des petites entreprises peu protégées, ou exploitant une faille applicative spécifique (crash).
- **DDoS** : Utilisé par des groupes cybercriminels organisés, des hacktivistes ou des États dans le cadre de guerres hybrides, d'extorsions financières (Ransom DDoS) ou de diversions pour masquer une exfiltration de données.

## Bonnes pratiques de défense
- **Pour le DoS** : Maintenir les pare-feux actifs, configurer des seuils de connexion par IP (*rate limiting*) et patcher régulièrement les serveurs.
- **Pour le DDoS** : Souscrire à une solution de protection cloud spécialisée, utiliser la répartition de charge géographique (Anycast) et mettre en place des plans de réponse aux incidents avec son hébergeur/FAI.

## Conclusion
Le DoS est un problème de sécurité locale que l'on peut résoudre au niveau du serveur ou du pare-feu de l'entreprise. Le DDoS, en revanche, est un problème d'infrastructure réseau globale qui nécessite des capacités de filtrage déportées et massives, souvent fournies par des opérateurs de télécommunications ou des CDN de sécurité spécialisés.