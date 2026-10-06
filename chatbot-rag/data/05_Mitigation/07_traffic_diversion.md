# Déviation de trafic (Traffic Diversion)

## Introduction
Mécanisme consistant à dérouter temporairement le trafic destiné à une entreprise vers une infrastructure de nettoyage externe uniquement lors de la détection d'une attaque.

## Fiche Technique
| Type d'activation | Latence hors attaque | Temps de réaction DDoS | Complexité réseau |
| :--- | :--- | :--- | :--- |
| **Always-On (Permanent)** | 5 à 15ms | Instantané (0 sec) | Moyenne |
| **On-Demand (Déviation)** | 0ms | 3 à 10 minutes | Élevée |

## Explications détaillées
### Principe et Fonctionnement
La déviation de trafic (ou Traffic Diversion) est le processus dynamique de redirection des flux réseau. En temps normal, le trafic des internautes s'écoule directement vers les serveurs de l'entreprise. Lorsqu'une attaque DDoS est détectée par les sondes de surveillance :
1. Le système de détection déclenche une alerte de déviation.
2. Le routage du bloc d'adresses IP de l'entreprise est modifié au niveau BGP mondial (en annonçant un chemin réseau passant par le centre de nettoyage). Alternativement, la modification peut se faire au niveau DNS (en changeant l'enregistrement A vers l'IP du CDN de protection).
3. Le trafic d'attaque et le trafic légitime sont ainsi déroutés vers l'infrastructure de filtrage.
4. Une fois l'attaque terminée, le routage est rétabli à sa configuration nominale.

### Rôle dans la mitigation DDoS
- **Économie de ressources** : Évite de faire passer tout le trafic par un centre de nettoyage coûteux en permanence (modèle "On-Demand").

### Avantages et Limites
- **Avantages** :
  - Coût d'abonnement moins élevé que les solutions permanentes (Always-On).
  - Aucune latence réseau ajoutée en période de fonctionnement normal hors attaque.
- **Limites** :
  - Délai d'activation : la propagation des nouvelles routes BGP ou du cache DNS peut prendre de 2 à 10 minutes pendant lesquelles le serveur d'origine subit l'attaque de plein fouet.

### Bonnes pratiques
1. Utiliser la déviation BGP pour les infrastructures critiques disposant de leurs propres blocs d'adresses IP (/24 minimum).
2. Pour les sites web classiques, préférer les solutions de type CDN toujours actives pour éliminer le délai d'activation.

## Bonnes pratiques de cybersécurité
1. Privilégier les solutions multi-points Always-On.
2. Éviter d'exposer l'IP réelle du serveur d'origine.
3. Automatiser les mécanismes de basculement de routage.

## Conclusion
La mitigation DDoS regroupe l'ensemble des techniques actives permettant d'annuler l'effet perturbateur d'une attaque en cours. Une combinaison efficace combine filtrage chirurgical (BGP Flowspec/SYN Cookies) et capacité d'absorption massive (Cloud Protection).
