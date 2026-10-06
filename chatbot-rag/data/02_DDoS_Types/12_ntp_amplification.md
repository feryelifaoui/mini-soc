# Attaque NTP Amplification

## Introduction
Exploite le protocole NTP et la commande monlist pour générer des flux d'attaque volumétriques hautement amplifiés.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 4 (Transport) & Couche 7 (Application) |
| **Protocole** | NTP (UDP 123) |
| **Facteur d'amplification** | x550 à x600 |
| **Cible** | Bande passante réseau de la victime |
| **Bande passante générée** | Extrêmement élevée (Volumétrique majeure) |

## Explications détaillées
### Principe et Fonctionnement
L'attaque par amplification NTP exploite une fonction de diagnostic du protocole de synchronisation temporelle NTP (Network Time Protocol).
1. L'attaquant cible des serveurs NTP publics vulnérables (souvent des versions anciennes de l'OS ou de l'application NTP).
2. L'attaquant envoie une requête contenant la commande obsolète `monlist` (ou `req_code 42`). Cette commande demande au serveur NTP de lui renvoyer la liste des 600 dernières adresses IP ayant communiqué avec lui.
3. L'attaquant usurpe l'adresse IP source (IP Spoofing) en utilisant l'adresse IP de la victime.
4. Le serveur NTP renvoie la liste complète des adresses IP découpée en plusieurs paquets UDP de grande taille vers la victime.
Le facteur d'amplification est l'un des plus élevés pour les protocoles standards : il peut atteindre un ratio de x550 (une requête de 234 octets génère plus de 120 kilooctets de données).

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Lien internet saturé en quelques secondes, impossibilité de joindre le réseau de l'entreprise.
- **Indicateurs clés** :
  - Flux massif de paquets UDP entrants provenant du port source 123.
  - Paquets contenant des structures de données de listes de serveurs NTP.

### Détection, Prévention et Mitigation
- **Détection** :
  - Alertes automatiques de pare-feu ou d'IDS signalant une hausse brutale du trafic UDP 123.
- **Prévention** :
  - Mettre à jour les serveurs NTP vers la version 4.2.7 ou ultérieure, où la commande `monlist` est désactivée par défaut ou remplacée par `mrulist` nécessitant une authentification.
  - Restreindre l'accès aux serveurs NTP via des directives de configuration strictes (`disable monitor` dans `ntp.conf`).
- **Mitigation** :
  - Blocage du port source UDP 123 en amont chez le FAI ou au niveau du routeur frontière de l'entreprise.

### Limites des protections
Le blocage absolu du port source 123 empêche la synchronisation horaire légitime de vos serveurs internes si celle-ci s'effectue avec des serveurs de temps publics externes sur Internet.


## Exemple Concret
```text
# Extrait de configuration ntp.conf sécurisé pour empêcher le détournement :
restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque NTP Amplification (Couche 4 (Transport) / Couche 7 (Application)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
