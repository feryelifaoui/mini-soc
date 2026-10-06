# Attaque ICMP Flood

## Introduction
Sature les ressources réseau et CPU en envoyant des requêtes ICMP Echo Request (Ping) à grande vitesse.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 3 (Réseau) |
| **Protocole** | ICMP (Internet Control Message Protocol) |
| **Cible** | Bande passante réseau, Processeur |
| **Impact CPU** | Moyen |
| **Bande passante requise** | Moyenne à Élevée |

## Explications détaillées
### Principe et Fonctionnement
L'attaque ICMP Flood (ou Ping Flood) consiste à inonder une cible avec un grand nombre de paquets ICMP de type 8 (Echo Request, plus communément appelé "Ping"). Pour chaque requête reçue, le serveur cible est programmé pour répondre par un paquet ICMP de type 0 (Echo Reply). L'attaque consomme à la fois la bande passante descendante de la cible (flux de requêtes) et sa bande passante montante (flux de réponses), tout en épuisant les ressources CPU du serveur qui doit traiter chaque paquet et formuler les réponses.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Hausse spectaculaire du temps de latence réseau (RTT), déconnexions intempestives, saturation du processeur des routeurs et pare-feux périphériques.
- **Indicateurs clés** :
  - Quantité massive de paquets ICMP Echo Request entrants.
  - Taux élevé de paquets ICMP Echo Reply sortants.
  - Présence d'adresses IP sources fragmentées ou falsifiées.

### Détection, Prévention et Mitigation
- **Détection** :
  - Détection d'anomalies de protocole sur la couche 3 (Network).
  - Outils de monitoring (ex: Zabbix, Prometheus) signalant une alerte sur le volume de paquets ICMP par seconde.
- **Prévention** :
  - Configurer les routeurs et pare-feux pour rejeter ou limiter le trafic ICMP de type 8 (Echo Request) provenant d'Internet.
  - Désactiver la réponse aux requêtes de diffusion ICMP (Directed Broadcasts) pour éviter l'amplification.
- **Mitigation** :
  - Blocage pur et simple des requêtes ICMP entrantes au niveau du pare-feu de premier niveau (périmètre).
  - Configuration de la limitation de débit ICMP (`rate limiting`) au niveau du noyau de l'OS.

### Limites des protections
Désactiver ou bloquer ICMP de manière agressive peut gêner le diagnostic réseau légitime (les outils comme `ping` ou `traceroute` ne fonctionneront plus) et perturber le protocole PMTUD (Path MTU Discovery) qui s'appuie sur ICMP type 3 code 4.


## Exemple Concret
```bash
# Désactiver temporairement les réponses au Ping (ICMP Echo Request) sous Linux
sysctl -w net.ipv4.icmp_echo_ignore_all=1

# Limiter la réception de paquets ICMP à 10 par seconde via iptables
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 10/s -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque ICMP Flood (Couche 3 (Réseau)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
