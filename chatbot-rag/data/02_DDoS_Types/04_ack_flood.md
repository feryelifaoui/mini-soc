# Attaque ACK Flood

## Introduction
Sature les tables d'état des pare-feux en envoyant des paquets TCP ACK orphelins.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 4 (Transport) |
| **Protocole** | TCP (Transmission Control Protocol) |
| **Cible** | Table d'états du pare-feu, Processeur |
| **Impact CPU** | Très Élevé (pour les pare-feux Stateful) |
| **Bande passante requise** | Moyenne à Élevée |

## Explications détaillées
### Principe et Fonctionnement
Une attaque ACK Flood consiste à inonder un serveur ou un équipement de sécurité avec de faux paquets TCP portant le drapeau `ACK` (Acknowledgment). Normalement, un paquet ACK est envoyé par un client pour confirmer la réception de données après l'établissement d'une session TCP. Dans le cadre d'un ACK Flood, ces paquets sont "orphelins" ou "factices" : ils ne correspondent à aucune session active dans la table d'états (state table) du pare-feu ou du serveur. L'équipement cible doit analyser chaque paquet entrant, le comparer à sa table d'états et, constatant qu'il ne correspond à aucune session connue, le rejeter. Cette vérification constante et massive sature la mémoire RAM et le processeur des pare-feux à états (Stateful Firewalls).

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Plantage ou redémarrage des pare-feux, perte totale de connectivité réseau vers l'ensemble de l'infrastructure, baisse des performances réseau.
- **Indicateurs clés** :
  - Trafic entrant composé majoritairement de paquets TCP avec uniquement le flag `ACK` activé.
  - Numéros de séquence TCP aléatoires ou invalides dans les paquets reçus.
  - CPU du pare-feu ou du routeur proche de 100%.

### Détection, Prévention et Mitigation
- **Détection** :
  - Surveillance des compteurs d'états rejetés (state lookup failures) sur le pare-feu.
  - Analyse des paquets via tcpdump montrant des paquets ACK hors contexte.
- **Prévention** :
  - Utilisation de pare-feux sans état (Stateless Firewalls) pour le filtrage initial de premier niveau.
  - Architecture réseau redondante avec répartition de charge (Load Balancing).
- **Mitigation** :
  - **Mitigation Synproxy** : Utiliser des équipements dédiés capables de rejeter les ACK ne faisant pas suite à une poignée de main TCP validée.
  - Configuration de règles de pare-feu pour rejeter les paquets ACK invalides (sans connexion préexistante).

### Limites des protections
Le filtrage des paquets ACK nécessite une inspection approfondie de chaque paquet, ce qui consomme intrinsèquement des ressources CPU. Si le débit est trop élevé, la carte réseau elle-même peut saturer au niveau du matériel (NIC).


## Exemple Concret
```bash
# Exemple de détection rapide avec tcpdump (affiche les paquets ACK sans SYN)
tcpdump -i eth0 'tcp[tcpflags] & tcp-ack != 0 and tcp[tcpflags] & tcp-syn == 0' -n -c 100
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque ACK Flood (Couche 4 (Transport)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
