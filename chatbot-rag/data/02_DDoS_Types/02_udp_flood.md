# Attaque UDP Flood

## Introduction
Submerge la cible avec un grand volume de paquets UDP pour saturer la bande passante réseau et le CPU.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 4 (Transport) |
| **Protocole** | UDP (User Datagram Protocol) |
| **Cible** | Bande passante réseau, Processeur du routeur/serveur |
| **Impact CPU** | Moyen à Élevé (génération des paquets ICMP) |
| **Bande passante requise** | Élevée (Attaque typiquement volumétrique) |

## Explications détaillées
### Principe et Fonctionnement
Une attaque UDP Flood consiste à envoyer un grand nombre de paquets UDP (User Datagram Protocol) vers des ports aléatoires ou spécifiques de la machine cible. UDP étant un protocole sans connexion, le serveur récepteur doit traiter chaque paquet entrant en effectuant deux actions consommatrices :
1. Vérifier si une application écoute sur le port de destination.
2. Si aucune application n'écoute (cas le plus fréquent), générer et renvoyer un paquet ICMP de type 3 (Destination Unreachable - Port Unreachable).
Lorsque le flux de paquets UDP est massif, les ressources réseau (bande passante) et les processeurs de la cible et des pare-feux sont saturés par le traitement des paquets entrants et la génération des réponses ICMP.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Ralentissement extrême du réseau, saturation complète de la bande passante entrante (liens WAN), perte de paquets élevée.
- **Indicateurs clés** :
  - Volume énorme de paquets UDP entrants sur des ports non utilisés ou inhabituels.
  - Augmentation exponentielle des paquets ICMP sortants (Port Unreachable).
  - Les adresses IP sources sont souvent usurpées (IP Spoofing), rendant le filtrage par IP source inopérant.

### Détection, Prévention et Mitigation
- **Détection** :
  - Analyse des flux réseau (NetFlow/sFlow) montrant un pic anormal du ratio de trafic UDP par rapport à TCP.
  - Surveillance du trafic ICMP sortant.
- **Prévention** :
  - Limitation du débit de paquets ICMP générés au niveau du noyau de l'OS (`sysctl` sous Linux).
  - Fermeture ou désactivation des ports UDP non essentiels sur les pare-feux périmétriques.
- **Mitigation** :
  - Filtrage en amont chez le fournisseur d'accès internet (FAI) via des listes de contrôle d'accès (ACL).
  - Utilisation d'un centre de nettoyage (Scrubbing Center) capable d'absorber le trafic volumétrique et de ne laisser passer que le trafic légitime.
  - Rejet automatique des paquets UDP ne correspondant à aucun service actif connu.

### Limites des protections
Bloquer tout le trafic UDP peut paralyser les services légitimes basés sur UDP, tels que le DNS (port 53), le NTP (port 123) ou le protocole VPN (WireGuard, OpenVPN). La mitigation doit donc être sélective.


## Exemple Concret
```bash
# Exemple de règle de filtrage iptables pour limiter le trafic UDP entrant sur le port 53 (DNS)
iptables -A INPUT -p udp --dport 53 -m limit --limit 1000/s --limit-burst 2000 -j ACCEPT
iptables -A INPUT -p udp --dport 53 -j DROP
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque UDP Flood (Couche 4 (Transport)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
