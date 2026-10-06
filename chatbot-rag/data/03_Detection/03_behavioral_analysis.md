# Analyse comportementale (Behavioral Analysis)

## Introduction
Analyse de la nature et de l'intention des flux de données pour distinguer les utilisateurs légitimes des bots d'attaque.

## Fiche Technique
| Caractéristique | Détail |
| :--- | :--- |
| **Méthode** | Analyse de corrélation applicative et humaine |
| **Cible** | Attaques applicatives (L7), Bots, Slowloris |
| **Consommation CPU** | Élevée |
| **Précision** | Très Élevée |

## Explications détaillées
### Principe et Fonctionnement
Contrairement à la détection d'anomalies volumétriques simples, l'analyse comportementale s'intéresse à l'intention logique des transactions réseau. Elle examine la manière dont un client interagit avec une application. Par exemple, un bot HTTP Flood va demander une page web à haute fréquence sans télécharger les feuilles de style CSS, les scripts JS ou les images associés, et sans simuler de mouvements de souris ou de clics (comportement non humain). L'analyse comportementale étudie ces corrélations pour isoler et bloquer les flux suspects.

### Avantages et Limites
- **Avantages** :
  - Très efficace contre les attaques applicatives sophistiquées (L7).
  - Permet de maintenir l'accès des utilisateurs légitimes même au plus fort d'une attaque.
- **Limites** :
  - Nécessite une puissance de calcul importante pour analyser le trafic au niveau applicatif en temps réel.
  - Exige le déchiffrement du trafic HTTPS (SSL Offloading) pour inspecter le comportement applicatif.

### Bonnes pratiques
1. Déployer des outils d'analyse comportementale au niveau du WAF ou du CDN.
2. Implémenter des défis transparents (défi JavaScript silencieux) pour valider le comportement du navigateur.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
