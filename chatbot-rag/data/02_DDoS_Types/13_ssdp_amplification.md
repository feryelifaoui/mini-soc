# Attaque SSDP Amplification

## Introduction
Détourne les objets connectés compatibles UPnP exposés sur Internet pour inonder la victime.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 4 (Transport) & Couche 7 (Application) |
| **Protocole** | SSDP (UDP 1900) |
| **Facteur d'amplification** | x30 |
| **Cible** | Bande passante réseau de la victime |
| **Bande passante générée** | Moyenne à Élevée |

## Explications détaillées
### Principe et Fonctionnement
Le protocole SSDP (Simple Service Discovery Protocol) permet aux appareils de type Plug & Play (routeurs grand public, caméras IP, imprimantes, Smart TVs) de découvrir des services sur le réseau local via le port UDP 1900.
1. Les attaquants scannent Internet à la recherche d'appareils domestiques ou professionnels ayant exposé SSDP sur leur interface WAN (Internet) publique.
2. L'attaquant envoie une requête de recherche SSDP (type `M-SEARCH` ou `rootdevice`) à ces appareils en usurpant l'adresse IP source de sa victime.
3. Chaque appareil répond en envoyant la liste détaillée de ses services, formats et points de terminaison à l'adresse de la victime.
L'amplification est généralement d'un facteur x30. L'attaquant utilise des millions de périphériques IoT mal configurés pour concentrer un flux volumétrique important sur la cible.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Perte de connectivité réseau, surcharge du routeur frontal.
- **Indicateurs clés** :
  - Trafic UDP entrant important sur le port source 1900.
  - Paquets contenant des en-têtes HTTP/1.1 de type SSDP (ex: `HTTP/1.1 200 OK\r\nST: upnp:rootdevice`).

### Détection, Prévention et Mitigation
- **Détection** :
  - Capture de paquets identifiant la signature textuelle UPnP/SSDP sur le port 1900.
- **Prévention** :
  - Désactiver UPnP sur les routeurs et box internet domestiques ou professionnels.
  - S'assurer que le port UDP 1900 n'est jamais exposé publiquement sur Internet.
- **Mitigation** :
  - Filtrage et rejet automatique du trafic provenant du port source UDP 1900 en périphérie de réseau ou via un CDN de protection.

### Limites des protections
La prolifération constante d'objets connectés mal sécurisés chez les particuliers rend ce vecteur d'attaque toujours actif et difficile à tarir à la source.


## Exemple Concret
```bash
# Exemple de requête SSDP M-SEARCH envoyée par les attaquants (en UDP sur le port 1900)
# M-SEARCH * HTTP/1.1
# HOST: 239.255.255.250:1900
# MAN: "ssdp:discover"
# MX: 2
# ST: ssdp:all
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque SSDP Amplification (Couche 4 (Transport) / Couche 7 (Application)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
