# Attaque DNS Flood

## Introduction
Inonde les serveurs DNS de requêtes pour perturber la résolution de noms de domaine.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 7 (Application) |
| **Protocole** | DNS (UDP/TCP 53) |
| **Cible** | Serveurs DNS faisant autorité |
| **Impact CPU** | Élevé |
| **Bande passante requise** | Moyenne à Élevée |

## Explications détaillées
### Principe et Fonctionnement
Une attaque DNS Flood consiste à envoyer une quantité massive de requêtes de résolution de noms de domaine vers les serveurs DNS (Domain Name System) faisant autorité de la victime. L'attaquant configure son botnet pour envoyer des requêtes UDP sur le port 53. Afin de contourner la mise en cache (caching) du DNS et de forcer le serveur à effectuer des recherches intensives sur le disque ou des bases de données internes, les bots demandent souvent des sous-domaines inexistants générés aléatoirement (ex: `abcde123.nomdomaine.com`). Le serveur DNS passe du temps à traiter chaque requête pour finalement renvoyer une réponse d'erreur de type `NXDOMAIN` (Non-Existent Domain). Le serveur DNS est rapidement saturé, empêchant la résolution des requêtes DNS légitimes et rendant ainsi tous les services de l'entreprise (sites web, messagerie, APIs) invisibles sur Internet.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Résolution de nom impossible, latence réseau élevée, échecs de connexion des clients légitimes aux serveurs de l'entreprise.
- **Indicateurs clés** :
  - Pic massif de requêtes DNS (requêtes par seconde - QPS).
  - Taux anormal de réponses de type `NXDOMAIN` dans les statistiques du serveur DNS.
  - Requêtes ciblant des sous-domaines générés de manière aléatoire.

### Détection, Prévention et Mitigation
- **Détection** :
  - Surveillance du trafic réseau sur le port UDP/TCP 53.
  - Analyse des journaux de requêtes DNS (Query Logs).
- **Prévention** :
  - **DNS Anycast** : Distribuer l'infrastructure DNS sur plusieurs serveurs géographiquement répartis partageant la même adresse IP.
  - Mettre en place des mécanismes de limitation de débit des requêtes DNS (RRL - Response Rate Limiting) directement sur les serveurs DNS (BIND, PowerDNS).
- **Mitigation** :
  - Utiliser un service DNS de protection cloud géré (ex: Cloudflare DNS, AWS Route 53) capable d'absorber des volumes massifs de requêtes.
  - Bloquer les requêtes malformées au niveau du pare-feu.

### Limites des protections
Le filtrage des requêtes DNS peut être complexe car il est difficile de distinguer une requête légitime d'une requête malveillante sans analyser le contenu textuel de chaque demande, ce qui consomme du CPU.


## Exemple Concret
```bash
# Vérifier le volume de requêtes DNS reçues par un serveur BIND
rndc stats
# La commande génère un fichier de statistiques (souvent /var/named/data/named_stats.txt)
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque DNS Flood (Couche 7 (Application)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
