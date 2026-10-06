# Attaques par Amplification (Amplification Attacks)

## Introduction
Technique qui multiplie le volume du trafic réseau généré en exploitant l'asymétrie de taille entre requêtes et réponses de certains protocoles.

## Fiche Technique
| Protocole exploité | Facteur d'amplification typique |
| :--- | :--- |
| **SSDP** | x30 |
| **DNS** | x20 à x100 |
| **NTP** | x550 à x600 |
| **Memcached** | x10 000 à x51 000 |

## Explications détaillées
### Principe et Fonctionnement
Une attaque par amplification est une évolution directe de l'attaque par réflexion. Elle repose également sur l'usurpation d'adresse IP (IP Spoofing) et l'utilisation de serveurs intermédiaires. La particularité réside dans l'asymétrie de taille entre la requête envoyée par l'attaquant et la réponse générée par le serveur intermédiaire : la réponse est nettement plus grande que la requête.
L'attaquant envoie une requête de petite taille (ex: 50 octets) et force le serveur intermédiaire à envoyer une réponse géante (ex: 3 000 octets) à la victime. La bande passante de l'attaquant est ainsi multipliée ("amplifiée") par un facteur d'amplification spécifique au protocole utilisé (DNS, NTP, Memcached).

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Saturation totale et subite de l'infrastructure réseau de la victime, paquets légitimes jetés en masse en amont.
- **Indicateurs clés** :
  - Trafic volumétrique massif constitué de paquets UDP uniformes provenant de ports de protocoles connus (53, 123, 1900, 11211).

### Détection, Prévention et Mitigation
- **Détection** :
  - Outils de surveillance de bande passante (NMS) signalant des pics de trafic anormaux.
- **Prévention** :
  - Sécurisation globale des infrastructures internet (désactivation des services non requis, application des correctifs).
- **Mitigation** :
  - **Null Routing (Blackholing)** : Rejeter tout le trafic destiné à l'IP ciblée au niveau du FAI de transit (méthode de dernier recours car elle rend la cible indisponible).
  - Utilisation de réseaux de diffusion de contenu (CDN) et de services de nettoyage cloud (Scrubbing).

### Limites des protections
L'amplification permet à des attaquants disposant de faibles ressources matérielles de générer des attaques de niveau étatique (centaines de Gbps), rendant la protection locale (On-Premise) insuffisante.


## Exemple Concret
```text
# Formule mathématique du facteur d'amplification (BAP - Bandwidth Amplification Factor)
# BAP = Taille du paquet de réponse / Taille du paquet de requête
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaques par Amplification (Amplification Attacks) (Couche 4 (Transport) / Couche 7 (Application)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
