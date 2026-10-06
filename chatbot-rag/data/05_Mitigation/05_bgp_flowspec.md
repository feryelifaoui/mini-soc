# BGP Flowspec

## Introduction
Extension du protocole de routage BGP permettant de distribuer des règles de filtrage de paquets réseau complexes directement aux routeurs des FAI.

## Fiche Technique
| Paramètre | BGP Blackholing | BGP Flowspec |
| :--- | :--- | :--- |
| **Cible du blocage** | Adresse IP entière (destination) | Flux spécifique (IP, Port, Protocole, Taille) |
| **Précision** | Grossière (bloque tout) | Chirurgicale (bloque uniquement l'attaque) |
| **Complexité routeurs**| Faible | Moyenne à élevée |

## Explications détaillées
### Principe et Fonctionnement
BGP Flowspec (BGP Flow Specification) est défini par la RFC 8955. Il permet aux ingénieurs réseau d'envoyer des règles de filtrage très détaillées (similaires à des règles de pare-feu de couches 3/4) à travers le protocole BGP vers l'ensemble des routeurs d'un réseau ou vers les routeurs des fournisseurs d'accès internet (FAI) partenaires. Au lieu de simplement rediriger ou bloquer une IP entière (comme avec le Blackholing), BGP Flowspec permet de propager une règle du type : "Rejeter uniquement les paquets UDP provenant du port source 123 et d'une taille de 234 octets destinés à l'IP X".

### Rôle dans la mitigation DDoS
- **Mitigation chirurgicale à la source** : Permet de bloquer l'attaque volumétrique au plus près de son émission (dans le réseau du FAI) avant qu'elle ne sature les liens physiques de l'entreprise cible.
- **Automatisation globale** : Propagation instantanée de règles défensives sur des centaines de routeurs d'infrastructure.

### Avantages et Limites
- **Avantages** :
  - Filtrage très précis n'impactant pas le trafic légitime sur d'autres ports ou protocoles.
  - Exécuté directement au niveau matériel des routeurs de transit (très performant).
- **Limites** :
  - Tous les FAI ne permettent pas à leurs clients d'annoncer des règles Flowspec (pour des raisons de sécurité et de stabilité des routeurs).

### Bonnes pratiques
1. Définir des règles Flowspec temporaires avec un délai de validité automatique pour éviter l'encombrement des tables de routage.
2. Valider la syntaxe des règles avant toute diffusion globale.

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
