# Pare-feu (Firewall)

## Introduction
Équipement de sécurité filtrant les flux réseau entrants et sortants selon des règles prédéfinies.

## Fiche Technique
| Type de Pare-feu | Couche OSI ciblée | Fonction principale | vulnérabilité DDoS |
| :--- | :--- | :--- | :--- |
| **Stateless (Sans état)** | L3 / L4 | Filtrage de paquets simple | Aucune (très résilient) |
| **Stateful (Avec état)** | L4 | Suivi des sessions TCP | Saturation de la table d'états |
| **NGFW (Nouvelle Gén.)** | L4 à L7 | Inspection applicative, IPS | Surcharge CPU |

## Explications détaillées
### Principe et Fonctionnement
Un pare-feu (Firewall) agit comme un point de contrôle à la frontière du réseau. Il examine les en-têtes des paquets réseau (adresses IP sources/destinations, ports TCP/UDP, protocoles) et décide de les laisser passer (Allow/Pass) ou de les bloquer (Drop/Reject) en fonction d'une politique de sécurité prédéfinie (les listes d'accès ou ACL). Les pare-feux modernes peuvent être avec état (Stateful, qui surveillent le cycle de vie des connexions TCP) ou de nouvelle génération (NGFW - Next-Generation Firewall, capables d'inspecter les applications).

### Rôle dans la prévention DDoS
Le pare-feu périmétrique est la première barrière de défense. Il permet de :
- Bloquer immédiatement le trafic réseau dirigé vers des ports fermés ou sensibles (ex. SSH, RDP) depuis Internet.
- Appliquer des limitations élémentaires de débit par IP (Rate Limiting).
- Détecter et rejeter les paquets malformés ou non conformes.

### Avantages et Limites
- **Avantages** :
  - Protection robuste de bas niveau (Couches 3/4).
  - Traitement rapide à l'échelle du réseau local.
- **Limites** :
  - Sensible à la saturation de sa table d'états (Stateful) en cas d'attaque SYN/ACK Flood massive.
  - Incapable d'analyser le contenu applicatif complexe (Couche 7) de manière performante sans dégrader ses performances.

### Bonnes pratiques
1. Configurer une politique de sécurité restrictive par défaut ("Default Deny").
2. Placer le pare-feu en amont d'un répartiteur de charge capable de ventiler le trafic.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
