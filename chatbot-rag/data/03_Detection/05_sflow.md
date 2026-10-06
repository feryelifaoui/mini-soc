# sFlow (Sampled Flow)

## Introduction
Technologie d'échantillonnage de paquets réseau pour la surveillance à haute vitesse des commutateurs et routeurs.

## Fiche Technique
| Paramètre | Description |
| :--- | :--- |
| **Standard** | RFC 3176 (Multi-constructeurs) |
| **Port typique** | UDP 6343 |
| **Méthode** | Échantillonnage statistique de paquets |
| **Usage DDoS** | Analyse temps réel d'attaques volumétriques massives |

## Explications détaillées
### Principe et Fonctionnement
Contrairement à NetFlow qui comptabilise tous les flux, sFlow utilise un mécanisme d'**échantillonnage statistique**. Le commutateur ou le routeur configuré avec sFlow extrait un paquet de manière aléatoire sur un intervalle défini (par exemple, 1 paquet sur 1000). Les en-têtes de ce paquet échantillonné sont immédiatement encapsulés dans un paquet UDP et envoyés au collecteur sFlow. sFlow fonctionne au niveau de la puce réseau (ASIC) des équipements, ce qui lui permet de surveiller des réseaux à très haut débit (10 Gbps, 100 Gbps+) sans impact CPU.

### Avantages et Limites
- **Avantages** :
  - Scalabilité extrême : idéal pour les réseaux de centres de données et les cœurs de réseaux d'opérateurs.
  - Traitement en temps réel (pas de mise en cache interne sur l'équipement).
- **Limites** :
  - Précision statistique : des attaques de très faible volume ou très courtes (micro-bursts) peuvent passer inaperçues si elles ne sont pas échantillonnées.

### Bonnes pratiques
1. Ajuster le taux d'échantillonnage en fonction de la bande passante de l'interface (ex: 1/1000 pour du 10G, 1/10000 pour du 100G).
2. Déployer sFlow sur les commutateurs de distribution.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
