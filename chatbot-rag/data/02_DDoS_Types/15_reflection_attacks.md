# Attaques par Réflexion (Reflection Attacks)

## Introduction
Masque l'identité de l'attaquant et redirige le trafic réseau vers la victime en utilisant des serveurs tiers intermédiaires.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 3 (Réseau) & Couche 4 (Transport) |
| **Mécanisme** | IP Spoofing + Utilisation de serveurs intermédiaires |
| **Cible** | Bande passante et CPU de la victime |
| **Avantage Attaquant** | Anonymat total, pas de lien direct |

## Explications détaillées
### Principe et Fonctionnement
Une attaque par réflexion (Reflection Attack) repose sur l'utilisation d'équipements tiers (serveurs, routeurs, objets connectés légitimes) agissant comme des miroirs réseau ("réflecteurs"). L'attaquant envoie des paquets réseau à ces réflecteurs en falsifiant l'adresse IP source de ses paquets avec celle de la victime (IP Spoofing). Lorsque les réflecteurs reçoivent la requête, ils répondent naturellement en envoyant leur paquet de réponse à l'adresse IP source spécifiée, c'est-à-dire vers la victime.
L'attaquant n'interagit jamais directement avec la victime, ce qui lui assure un haut niveau d'anonymat et complique les tentatives de traçabilité géographique.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Ralentissement du réseau, saturation des ports d'entrée du serveur.
- **Indicateurs clés** :
  - Réception de réponses réseau à des requêtes que la victime n'a jamais initiées (ex: réponses DNS, paquets TCP SYN-ACK orphelins).
  - Le trafic entrant provient de milliers de serveurs tiers légitimes (ex: serveurs DNS de Google, serveurs NTP publics).

### Détection, Prévention et Mitigation
- **Détection** :
  - Inspection de paquets pour identifier les flux de type "Réponse" (Response/Reply) non sollicités.
- **Prévention** :
  - **Déploiement de BCP 38** au niveau global pour empêcher l'émission de paquets à IP source usurpée.
- **Mitigation** :
  - Configuration de règles de pare-feu pour bloquer ou limiter les paquets de réponse non sollicités (ex. rejet des SYN-ACK sans SYN sortant correspondant).
  - Utilisation d'un service de protection cloud pour faire face au volume distribué.

### Limites des protections
L'attaquant peut changer de type de réflecteur très facilement (passer de DNS à NTP, puis à SSDP), ce qui exige des systèmes de protection flexibles et polyvalents.


## Exemple Concret
```bash
# Capture tcpdump pour isoler les paquets de réponse DNS entrants suspects
tcpdump -i eth0 'src port 53 and udp' -n
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaques par Réflexion (Reflection Attacks) (Couche 3 (Réseau) / Couche 4 (Transport)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
