# IPFIX (IP Flow Information Export)

## Introduction
Le standard IETF officiel pour la mesure et l'export d'informations de flux IP, successeur spirituel de NetFlow v9.

## Fiche Technique
| Paramètre | Description |
| :--- | :--- |
| **Standard** | RFC 7011 / RFC 7012 (IETF) |
| **Port typique** | UDP/TCP 4739 |
| **Flexibilité** | Très élevée (Champs personnalisés) |
| **Usage DDoS** | Corrélation multi-couches et détection applicative |

## Explications détaillées
### Principe et Fonctionnement
IPFIX est le protocole standardisé par l'IETF basé sur NetFlow version 9. Il définit la manière dont les informations de flux IP sont formatées et exportées depuis un exportateur (routeur/pare-feu) vers un collecteur. IPFIX est beaucoup plus flexible que NetFlow : il permet de définir des champs personnalisés pour exporter des données de couche 7 (ex: le nom de domaine demandé dans une requête DNS, ou l'URI HTTP), ce qui le rend particulièrement puissant pour la détection d'attaques applicatives et protocolaires complexes.

### Avantages et Limites
- **Avantages** :
  - Standard ouvert et interopérable (compatible avec tous les grands constructeurs réseau).
  - Extensible : permet d'intégrer des informations de sécurité applicative dans les métadonnées de flux.
- **Limites** :
  - Configuration plus complexe en raison de la gestion des gabarits (Templates) de données personnalisés.

### Bonnes pratiques
1. Privilégier IPFIX dans les environnements multi-constructeurs pour harmoniser la collecte de données.
2. Configurer les templates IPFIX pour exporter les ID de VLAN et les informations de protocole applicatif.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
