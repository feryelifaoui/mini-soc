# Fonctionnement général d'une attaque DDoS

## Introduction
Pour contrer efficacement une attaque DDoS, il est essentiel de comprendre son fonctionnement interne. Le mécanisme repose sur l'exploitation des limites de capacité physiques et logiques des infrastructures informatiques, associées à une coordination rigoureuse des sources d'attaque.

## Explications détaillées

### 1. La phase de préparation : Construction du Botnet
Avant de lancer une attaque, l'attaquant doit réunir une puissance de frappe suffisante.
1. **Le Scan** : Des scripts automatisés parcourent Internet à la recherche de systèmes vulnérables (systèmes non patchés, objets connectés avec mots de passe par défaut).
2. **L'Infection** : Une fois la faille identifiée, un malware (botnet agent) est injecté sur la machine cible.
3. **L'Enrôlement** : La machine infectée (le "bot") se connecte au serveur de Command & Control (C2) de l'attaquant et attend les instructions.

### 2. La phase de commande : Le déclenchement
L'attaquant décide de cibler une victime spécifique (adresse IP ou nom de domaine).
1. **L'ordre** : L'attaquant envoie une commande cryptée ou masquée aux serveurs C2.
2. **La propagation** : Les serveurs C2 répercutent l'ordre de ciblage à l'ensemble des bots actifs du réseau.
3. **Le choix de l'attaque** : L'ordre spécifie le type d'attaque (ex: SYN Flood sur le port 443, HTTP Flood sur une URL spécifique) et la durée.

### 3. La phase d'assaut : La saturation
Les bots commencent à envoyer simultanément des flux de paquets vers la victime. Le système de la victime subit alors plusieurs goulots d'étranglement :

- **Saturation des liens réseau (Bande passante)** : Les tuyaux d'arrivée internet de la victime sont pleins. Les paquets légitimes des vrais utilisateurs sont rejetés par les routeurs en amont car il n'y a plus de place physique.
- **Saturation des tables d'état (Pare-feu / Équipements de sécurité)** : Les pare-feux à états (stateful) doivent suivre chaque connexion. Face à des millions de connexions simulées, leur mémoire RAM s'épuise et ils cessent de fonctionner (blocage total).
- **Épuisement des ressources serveur (CPU/RAM/Base de données)** : Au niveau applicatif, le serveur web tente de répondre à chaque requête en exécutant du code PHP/Python/Java et en interrogeant la base de données, ce qui s'achève par un crash applicatif.

```
+---------------+     +---------------+     +--------------------+
|  Attaquant    | --> |  Serveur C2   | --> | Botnet (Bots 1..N) |
+---------------+     +---------------+     +--------------------+
                                                      |
                                                      v
                                            +--------------------+
                                            | Trafic saturant    |
                                            +--------------------+
                                                      |
                                                      v
                                            +--------------------+
                                            |   CIBLE (Victime)  |
                                            +--------------------+
```

## Exemples concrets
- **Attaque volumétrique** : Envoi massif de paquets UDP de 1500 octets (taille MTU maximale) pour remplir la bande passante du routeur de l'entreprise.
- **Attaque protocolaire** : Envoi de paquets TCP SYN. Le serveur ouvre une connexion à chaque fois et attend le ACK final. Le serveur sature sa table de connexions semi-ouvertes (*backlog table*) en quelques secondes.

## Tableau de l'impact sur les composants d'infrastructure
| Composant | Type de ressource menacée | Symptôme typique |
| :--- | :--- | :--- |
| **Lien WAN (Transit FAI)** | Bande passante (Gbps) | Perte de paquets importante, latence élevée (ping > 1000ms) |
| **Pare-feu (Firewall)** | Table d'états, CPU | Console d'administration inaccessible, redémarrage de l'équipement |
| **Serveur Web** | File d'attente TCP, Threads CPU | Erreurs HTTP 502 Bad Gateway, 504 Gateway Timeout |
| **Base de données** | Pool de connexions SQL | Blocage des requêtes en attente de verrous, crash du service SQL |

## Bonnes pratiques de prévention
1. **Architecture distribuée** : Éviter les points de défaillance uniques (*Single Point of Failure*).
2. **Détection précoce** : Configurer des alertes basées sur le trafic réseau anormal (NetFlow/sFlow).
3. **Collaboration avec le FAI** : Mettre en place des protocoles d'atténuation d'urgence avec les fournisseurs réseau en amont.

## Conclusion
Le fonctionnement général d'une attaque DDoS repose sur la asymétrie de puissance : un attaquant coordonne de multiples sources pour surcharger un point centralisé. La défense doit donc elle aussi être décentralisée et s'appuyer sur des architectures capables d'absorber et de disperser cette charge de manière intelligente.