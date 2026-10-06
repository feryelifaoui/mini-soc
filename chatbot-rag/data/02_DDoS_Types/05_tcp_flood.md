# Attaque TCP Flood (Autres Flags)

## Introduction
Utilise des combinaisons inhabituelles de drapeaux TCP pour perturber la pile réseau des serveurs et pare-feux.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 4 (Transport) |
| **Protocole** | TCP (Transmission Control Protocol) |
| **Cible** | Pile TCP/IP du noyau (Kernel), CPU |
| **Impact CPU** | Élevé (analyse complexe des paquets) |
| **Bande passante requise** | Moyenne |

## Explications détaillées
### Principe et Fonctionnement
Les attaques TCP Flood (autres que SYN et ACK) englobent l'utilisation de paquets TCP contenant des combinaisons de drapeaux (flags) invalides ou inhabituelles, telles que :
- **FIN Flood** : Envoi de paquets avec le flag `FIN` (demande de fermeture de connexion) pour forcer le serveur à chercher une session active correspondante afin de la fermer.
- **RST Flood** : Envoi de paquets `RST` (Reset) pour forcer la fermeture de connexions légitimes de vrais utilisateurs.
- **PUSH-ACK Flood** : Utilise le flag `PSH` pour forcer le système d'exploitation à envoyer immédiatement les données de paquets vides aux applications, surchargeant les tampons mémoire.
- **Xmas Attack** : Paquets TCP ayant tous les flags activés (SYN, FIN, RST, PSH, URG, ECE, CWR), ressemblant à "un arbre de Noël allumé". La pile réseau de la cible doit dépenser beaucoup de ressources CPU pour interpréter ces paquets non conformes aux normes RFC.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Déconnexions en cascade d'utilisateurs légitimes, latence élevée, instabilité de la pile réseau de l'OS.
- **Indicateurs clés** :
  - Distribution anormale de flags TCP dans le trafic entrant (ex. pics de paquets RST ou FIN).
  - Présence de paquets TCP invalides ou malformés dans les captures de trafic.

### Détection, Prévention et Mitigation
- **Détection** :
  - Règles IDS (Snort/Suricata) écrites spécifiquement pour identifier les combinaisons illégitimes de drapeaux TCP.
- **Prévention** :
  - Durcissement de la configuration réseau du noyau de l'OS (Network Stack Hardening).
- **Mitigation** :
  - Configurer le pare-feu pour rejeter immédiatement les paquets TCP non conformes (ex: drapeaux invalides).
  - Utilisation de pare-feux de type "Connection-Tracking" capables d'ignorer les paquets hors session.

### Limites des protections
Certaines applications réseau légitimes mal codées peuvent parfois envoyer des paquets TCP non conformes. Un filtrage trop strict peut générer des faux positifs.


## Exemple Concret
```bash
# Règle iptables pour bloquer les paquets "Xmas" (tous les flags activés)
iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP

# Règle iptables pour bloquer les paquets "Null" (aucun flag activé)
iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque TCP Flood (Autres Flags) (Couche 4 (Transport)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
