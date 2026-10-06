# Attaque Memcached Amplification

## Introduction
Exploite les serveurs de cache Memcached mal configurés pour obtenir des facteurs d'amplification records dépassant 10 000.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 4 (Transport) & Couche 7 (Application) |
| **Protocole** | Memcached (UDP 11211) |
| **Facteur d'amplification** | x10 000 à x51 000 |
| **Cible** | Bande passante réseau de la victime |
| **Bande passante générée** | Extrême (Atteint rapidement plusieurs centaines de Gbps) |

## Explications détaillées
### Principe et Fonctionnement
Memcached est un système de cache en mémoire open-source couramment utilisé pour accélérer les applications web dynamiques. Par défaut, certaines anciennes installations de Memcached écoutaient sur le port UDP 11211.
1. L'attaquant se connecte à un serveur Memcached public mal configuré.
2. Il enregistre une valeur très volumineuse (par exemple, 1 Mo de données aléatoires) associée à une clé spécifique via TCP.
3. Ensuite, l'attaquant envoie une multitude de requêtes de lecture de cette clé (`get`) en UDP, en usurpant l'adresse IP source de sa victime.
4. Le serveur Memcached renvoie la valeur volumineuse (de 1 Mo) à la victime.
Cette technique offre un facteur d'amplification record pouvant aller de x10 000 à x51 000. Une attaque de quelques mégabits par seconde initiée par l'attaquant se transforme en un raz-de-marée de plusieurs centaines de gigabits par seconde contre la victime.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Écroulement complet et instantané des routeurs, pare-feux et liaisons internet de l'entreprise cible.
- **Indicateurs clés** :
  - Flux entrant de paquets UDP massifs provenant du port source 11211.
  - Paquets contenant les données binaires ou textuelles typiques du protocole Memcached.

### Détection, Prévention et Mitigation
- **Détection** :
  - Détection volumétrique immédiate au niveau des routeurs frontières.
- **Prévention** :
  - **Désactiver UDP sur Memcached** : Configurer Memcached pour écouter exclusivement sur localhost (127.0.0.1) et désactiver l'écoute UDP (ajouter `-U 0` au démarrage de Memcached).
  - Pare-feu restrictif bloquant le port 11211 pour tout trafic externe.
- **Mitigation** :
  - Rejet complet du trafic UDP 11211 au niveau des transitaires IP (FAI) via des règles de filtrage d'urgence (ACL / BGP Flowspec).

### Limites des protections
L'attaque est si violente qu'elle dépasse instantanément la capacité physique de traitement de la plupart des pare-feux d'entreprise On-Premise. Seuls les CDN mondiaux et les FAI de transit peuvent l'atténuer.


## Exemple Concret
```bash
# Désactiver le port UDP 11211 de Memcached (sous Debian/Ubuntu, éditer /etc/memcached.conf)
# Remplacer ou ajouter :
-l 127.0.0.1
-U 0
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque Memcached Amplification (Couche 4 (Transport) / Couche 7 (Application)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
