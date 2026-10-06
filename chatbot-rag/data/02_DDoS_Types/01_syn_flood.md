# Attaque SYN Flood

## Introduction
Exploite le mécanisme de handshake TCP à trois voies pour épuiser les ressources de connexion du serveur.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 4 (Transport) |
| **Protocole** | TCP (Transmission Control Protocol) |
| **Cible** | Pile réseau du système d'exploitation (Backlog) |
| **Impact CPU** | Faible à Moyen (si SYN Cookies activés) |
| **Bande passante requise** | Faible à Moyenne (quelques Mbps suffisent pour saturer un serveur non protégé) |

## Explications détaillées
### Principe et Fonctionnement
L'attaque SYN Flood exploite une faiblesse de la poignée de main TCP (Three-Way Handshake). L'attaquant envoie une multitude de requêtes de connexion TCP avec le drapeau `SYN` activé, souvent en utilisant des adresses IP sources usurpées (IP Spoofing). Le serveur cible répond en envoyant un paquet `SYN-ACK` et alloue des ressources en mémoire (dans la table des connexions semi-ouvertes, appelée *backlog table*) en attendant le paquet `ACK` final du client. L'attaquant n'envoie jamais ce `ACK` final. Par conséquent, les connexions restent dans l'état `SYN_RECV` (semi-ouvertes) jusqu'à ce qu'un délai de garde (timeout) expire. Le backlog se sature rapidement, empêchant les utilisateurs légitimes d'établir de nouvelles connexions TCP.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Serveur web ou applicatif indisponible, refus de connexion TCP ("Connection refused" ou timeout).
- **Indicateurs clés** :
  - Nombre anormalement élevé de connexions dans l'état `SYN_RECV` (vérifiable via `netstat -an | findstr SYN_RECV` ou `ss -antp`).
  - Pic élevé de trafic réseau constitué presque exclusivement de paquets TCP SYN de petite taille (souvent 40 à 60 octets).
  - Taux de perte de paquets élevé sur les connexions entrantes.

### Détection, Prévention et Mitigation
- **Détection** :
  - Analyse des journaux réseau et des métriques de pile TCP.
  - Alertes IDS/IPS basées sur le nombre de paquets SYN par seconde par IP source.
- **Prévention** :
  - **SYN Cookies** : Le serveur n'alloue plus de mémoire dans le backlog à la réception du SYN. Il chiffre les informations de connexion dans le numéro de séquence initial TCP du SYN-ACK. Si le client est légitime, il renvoie un ACK contenant ce cookie décryptable par le serveur qui ouvre alors la connexion.
  - Augmentation de la taille de la table de backlog (`sysctl -w net.ipv4.tcp_max_syn_backlog=20480`).
  - Réduction du délai de timeout des connexions semi-ouvertes (`sysctl -w net.ipv4.tcp_synack_retries=2`).
- **Mitigation** :
  - Filtrage des paquets SYN suspects par un pare-feu ou un CDN Anycast en amont.
  - Recours à un proxy TCP (ex: HAProxy ou F5 BIG-IP) agissant comme bouclier et ne transmettant les connexions au serveur final que lorsqu'elles sont entièrement établies.

### Limites des protections
Les SYN Cookies peuvent ajouter une surcharge CPU mineure sur le serveur en cas d'attaque massive. De plus, ils désactivent certaines options TCP avancées (comme les fenêtres de taille étendue) si elles ne sont pas gérées par le noyau.


## Exemple Concret
```bash
# Commande Linux pour lister les connexions à l'état SYN_RECV
ss -n state syn-recv

# Règle iptables basique pour limiter le taux de paquets SYN entrants
iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 4 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque SYN Flood (Couche 4 (Transport)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
