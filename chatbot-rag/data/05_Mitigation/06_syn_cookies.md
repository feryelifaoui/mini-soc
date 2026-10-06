# SYN Cookies

## Introduction
Mécanisme de défense réseau au niveau du noyau de l'OS permettant de résister aux attaques de type SYN Flood sans saturer le backlog TCP.

## Fiche Technique
| Paramètre réseau Linux | Valeur recommandée | Rôle de sécurité |
| :--- | :--- | :--- |
| `net.ipv4.tcp_syncookies` | `1` | Active le mécanisme de SYN Cookies |
| `net.ipv4.tcp_synack_retries`| `2` | Réduit les tentatives de SYN-ACK non répondus |
| `net.ipv4.tcp_max_syn_backlog`| `20480` | Augmente la taille de la table de backlog |

## Explications détaillées
### Principe et Fonctionnement
Normalement, lorsqu'un serveur reçoit un paquet TCP SYN, il stocke les informations de la connexion naissante dans sa table de backlog (mémoire) et répond par un SYN-ACK. Lors d'une attaque SYN Flood, cette table sature en quelques secondes.
Lorsque les **SYN Cookies** sont activés :
1. À la réception du paquet SYN, le serveur n'alloue aucun espace mémoire dans sa table de backlog.
2. Il génère un numéro de séquence TCP initial (ISN) chiffré et calculé de manière mathématique (le "Cookie") contenant les paramètres clés de la connexion (IP source/dest, ports, horodatage, options TCP). Ce cookie est envoyé dans le paquet SYN-ACK.
3. Si le client est légitime, il répond par un paquet ACK. Ce paquet contient le numéro de séquence reçu plus un. Le serveur extrait cette valeur, en soustrait un, valide le cookie cryptographique et, si le calcul est correct, ouvre instantanément la connexion TCP dans sa table de session définitive.

### Rôle dans la mitigation DDoS
- **Résilience de la pile TCP** : Permet au serveur de continuer à accepter des connexions TCP légitimes même si le volume de requêtes SYN d'attaque dépasse la capacité mémoire physique de la machine.

### Avantages et Limites
- **Avantages** :
  - Consommation mémoire nulle pour les connexions semi-ouvertes.
  - Activation transparente pour les clients légitimes.
- **Limites** :
  - Légère surcharge CPU pour calculer et valider cryptographiquement chaque cookie.
  - Perte de certaines options TCP avancées (comme les timestamps ou les fenêtres d'échelle) dans les anciens noyaux de systèmes d'exploitation si le cookie doit être généré.

### Bonnes pratiques
1. Activer systématiquement les SYN Cookies dans la configuration réseau Linux (`sysctl -w net.ipv4.tcp_syncookies=1`).
2. S'assurer que le processeur de la machine dispose d'instructions de chiffrement rapides.

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
