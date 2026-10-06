# Analyse de l'attaque (Analysis Phase)

## Introduction
Investigation approfondie pour disséquer les vecteurs, l'intensité et les caractéristiques physiques de l'attaque DDoS.

## Fiche Technique
| Métrique analysée | Objectif défensif | Outil associé |
| :--- | :--- | :--- |
| **Vecteurs (Ports/Drapeaux)** | Déterminer la couche OSI ciblée | Wireshark / tshark |
| **BPS / PPS** | Choisir l'échelle de la mitigation | NetFlow / sFlow |
| **User-Agent / URI** | Écrire une règle de WAF (L7) | Logs d'accès Nginx/Apache |

## Explications détaillées
### Principe et Fonctionnement
Une fois l'incident identifié, la phase d'analyse vise à comprendre précisément comment l'attaque est menée afin de concevoir la contre-mesure la plus efficace. Les analystes du SOC examinent la capture de paquets (fichiers PCAP), les ports concernés, et la répartition géographique des sources d'attaque.

### Éléments clés de l'analyse DDoS
1. **Identification du vecteur** : S'agit-il d'un SYN Flood, d'une amplification NTP, d'un HTTP GET Flood, ou d'une combinaison multi-vectorielle ?
2. **Mesure de l'intensité** : Évaluer la bande passante (BPS) et le volume de paquets (PPS) pour déterminer si vos équipements locaux (On-Premise) peuvent traiter le filtrage ou s'il faut déporter la protection chez votre transitaire IP (FAI).
3. **Recherche de signatures uniques** : Trouver des constantes dans les paquets d'attaque (ex: valeur de TTL fixe, taille de paquet spécifique, chaîne de texte récurrente dans le payload, en-tête User-Agent HTTP particulier).
4. **Analyse de la source** : Cartographier les adresses IP attaquantes pour identifier les pays d'origine (GeoIP).

### Bonnes pratiques
1. Effectuer des captures de paquets (tcpdump) courtes (10-30 secondes) pour éviter de saturer le disque dur pendant les pics de trafic.
2. Utiliser des outils d'analyse automatisés pour extraire rapidement les adresses IP sources prédominantes.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
