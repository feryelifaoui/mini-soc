# Attaque DNS Amplification

## Introduction
Exploite les serveurs DNS ouverts pour multiplier la taille du trafic d'attaque dirigé vers la victime.

## Fiche Technique
| Caractéristique | Valeur / Détail |
| :--- | :--- |
| **Couche OSI** | Couche 4 (Transport) & Couche 7 (Application) |
| **Protocole** | DNS / UDP |
| **Facteur d'amplification** | x20 à x100 |
| **Cible** | Bande passante réseau de la victime |
| **Bande passante générée** | Très élevée (Volumétrique majeure) |

## Explications détaillées
### Principe et Fonctionnement
L'attaque par amplification DNS est une forme d'attaque par réflexion et amplification. L'attaquant n'envoie pas directement de trafic à la victime. À la place :
1. L'attaquant envoie de petites requêtes DNS à des serveurs DNS configurés comme "résolveurs ouverts" (Open Resolvers, qui répondent à n'importe quelle adresse IP publique).
2. Il utilise l'usurpation d'adresse IP (IP Spoofing) pour faire croire que la requête provient de l'adresse IP de la victime.
3. Les requêtes demandent des enregistrements volumineux (ex: type `ANY` ou avec extensions de sécurité `DNSSEC`).
4. Les résolveurs DNS envoient la réponse volumineuse à l'adresse IP usurpée (la victime).
Le facteur d'amplification peut aller de x20 à x100, ce qui signifie qu'une requête de 60 octets génère une réponse de 3 000 à 6 000 octets. Avec un petit botnet, l'attaquant peut ainsi saturer des liens réseau de plusieurs gigabits.

### Symptômes et Indicateurs (IOCs)
- **Symptômes** : Saturation instantanée de la bande passante entrante (liens WAN), perte complète de connectivité.
- **Indicateurs clés** :
  - Trafic entrant massif composé exclusivement de réponses DNS UDP (port source 53) dirigé vers des ports clients aléatoires de la victime.
  - Taux de trafic asymétrique (énorme volume entrant, aucun volume sortant initié).

### Détection, Prévention et Mitigation
- **Détection** :
  - Analyse NetFlow montrant une prédominance du port source UDP 53 entrant.
- **Prévention** :
  - **BCP 38 (Best Common Practice 38)** : Implémentation globale du filtrage d'IP source pour empêcher l'IP Spoofing (responsabilité des FAI).
  - Sécuriser ses propres serveurs DNS pour qu'ils ne soient pas des Open Resolvers.
- **Mitigation** :
  - **Filtrage en amont (FAI / Cloud Scrubbing)** : Demander aux fournisseurs réseau de bloquer ou de limiter le trafic provenant du port source UDP 53 s'il n'est pas attendu.
  - Utilisation de la redirection de trafic vers un centre de nettoyage.

### Limites des protections
Comme le trafic d'attaque est constitué de réponses DNS valides provenant de serveurs DNS légitimes du monde entier, il ne peut pas être bloqué simplement par liste noire d'adresses IP. Le filtrage doit se faire au niveau volumétrique par des fournisseurs de transit réseau.


## Exemple Concret
```bash
# Exemple de requête DNS utilisée par les attaquants pour tester l'amplification
dig ANY google.com @<adresse-serveur-dns-ouvert> +dnssec
```

## Bonnes pratiques de défense
1. Implémenter le rate limiting.
2. Collaborer avec le FAI pour le filtrage volumétrique.
3. Segmenter le réseau.

## Conclusion
L'attaque Attaque DNS Amplification (Couche 7 (Application) / Couche 4 (Transport)) demeure un vecteur d'attaque critique qui nécessite une protection robuste au niveau de l'infrastructure réseau ou applicative.
