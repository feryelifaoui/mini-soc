# Analyse de trafic (Traffic Analysis)

## Introduction
Techniques d'inspection en profondeur des paquets réseau (DPI) pour disséquer les attaques et construire des filtres d'atténuation précis.

## Fiche Technique
| Niveau d'analyse | Outil adapté | Objectif principal |
| :--- | :--- | :--- |
| **Inspection de paquets (DPI)**| Wireshark / tcpdump | Isoler une signature ou un motif répétitif dans le payload |
| **Analyse globale** | NetFlow / sFlow | Identifier la volumétrie et les tendances géographiques |
| **Analyse applicative** | WAF logs / Nginx | Identifier les schémas de requêtes HTTP répétitives |

## Explications détaillées
### Principe et Fonctionnement
L'analyse de trafic consiste à capturer des paquets réseau bruts à l'aide d'analyseurs de protocoles (ou "sniffers") pour examiner leur contenu exact. Contrairement aux métadonnées (NetFlow), l'analyse de trafic permet d'aller jusqu'à la couche 7 pour examiner le contenu (payload) des paquets. Pendant une attaque, l'analyse de trafic permet d'isoler une caractéristique unique et constante présente uniquement dans les paquets malveillants (ex: une chaîne de caractères spécifique dans la charge utile UDP). Cette signature servira à écrire une règle de filtrage ultra-précise au niveau du pare-feu pour bloquer l'attaque sans perturber le trafic légitime.

### Outils principaux
- **Wireshark** : Interface graphique idéale pour analyser des captures réseau (fichiers PCAP) de taille moyenne et comprendre les protocoles.
- **Tcpdump** : Outil en ligne de commande pour capturer le trafic réseau en temps réel directement sur les serveurs et les routeurs.

### Bonnes pratiques
1. Limiter la durée des captures en temps réel pendant une attaque pour éviter de saturer la mémoire RAM du serveur.
2. Utiliser des filtres d'affichage stricts pour isoler uniquement le trafic suspect du bruit de fond.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
