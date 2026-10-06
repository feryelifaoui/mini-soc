# Listes noires (Blacklisting)

## Introduction
Méthode de filtrage consistant à interdire l'accès à un groupe d'adresses IP, de pays ou d'identifiants identifiés comme hostiles.

## Fiche Technique
| Type de liste | Approche de sécurité | Risque de faux positifs | Risque de faux négatifs |
| :--- | :--- | :--- | :--- |
| **Blacklist (Exclusion)** | Permis par défaut, interdit si suspect | Faible | Élevé |
| **Whitelist (Inclusion)** | Interdit par défaut, autorisé si connu | Élevé | Très faible |

## Explications détaillées
### Principe et Fonctionnement
Le Blacklisting (ou listage d'exclusion) consiste à maintenir une base de données de sources malveillantes connues et à leur bloquer systématiquement l'accès au réseau ou à l'application. Cette liste peut être constituée d'adresses IP individuelles, de blocs d'adresses IP (CIDR), ou de noms de domaine.

### Rôle dans la prévention DDoS
- **Blocage de botnets connus** : Importer des flux de Threat Intelligence contenant la liste des adresses IP des serveurs C2 et des bots actifs pour les rejeter.
- **Réduction du bruit de fond** : Éviter que les scanners automatisés connus ne consomment des ressources sur vos serveurs.

### Avantages et Limites
- **Avantages** :
  - Simple à mettre en œuvre.
  - Permet d'éliminer une grande partie du trafic malveillant connu avant qu'il n'atteigne l'infrastructure critique.
- **Limites** :
  - Approche réactive : inefficace contre les adresses IP résidentielles propres utilisées pour la première fois par un botnet.
  - Les attaquants changent d'adresses IP très rapidement (rotation d'IP via des proxys ou des botnets mobiles).

### Bonnes pratiques
1. Mettre à jour les listes noires de manière automatisée (toutes les heures ou toutes les minutes) en s'appuyant sur des flux de sécurité réputés.
2. Associer un délai d'expiration aux IP bloquées pour éviter que la liste noire ne devienne trop volumineuse et ne ralentisse le traitement du pare-feu.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
