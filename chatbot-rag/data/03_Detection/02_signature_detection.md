# Détection par signatures (Signature Detection)

## Introduction
Identification des attaques DDoS en faisant correspondre le trafic entrant à des motifs (signatures) d'attaques connues.

## Fiche Technique
| Caractéristique | Détail |
| :--- | :--- |
| **Méthode** | Correspondance de motifs (Pattern Matching) |
| **Cible** | Outils d'attaque connus, exploits spécifiques |
| **Taux de faux positifs** | Très faible |
| **Détection Zero-Day** | Nulle |

## Explications détaillées
### Principe et Fonctionnement
La détection par signatures compare chaque paquet réseau entrant ou chaque requête HTTP à une base de données de motifs d'attaques connues. Une signature peut être une chaîne de caractères spécifique dans l'en-tête HTTP User-Agent, une taille de paquet réseau fixe et inhabituelle (ex: paquets UDP de 99 octets), ou une combinaison de drapeaux TCP invalides. C'est le principe de fonctionnement classique des pare-feux et des IDS traditionnels (comme Snort ou Suricata).

### Avantages et Limites
- **Avantages** :
  - Extrêmement précise : très faible taux de faux positifs pour les attaques connues.
  - Déclenchement d'alertes clair et explicite (le nom de l'attaque identifiée est immédiatement fourni aux analystes).
- **Limites** :
  - Inefficace contre les attaques nouvelles (Zero-Day) ou modifiées par l'attaquant.
  - Nécessite une mise à jour constante de la base de données de signatures.
  - Peut être contournée par des techniques d'obfuscation.

### Bonnes pratiques
1. Activer les mises à jour automatiques des règles IDS/IPS.
2. Utiliser des signatures spécifiques pour filtrer rapidement le bruit de fond internet connu.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
