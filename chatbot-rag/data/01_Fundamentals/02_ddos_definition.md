# Qu'est-ce qu'un DDoS (Distributed Denial of Service) ?

## Introduction
Une attaque par déni de service distribué (DDoS - Distributed Denial of Service) est une variante sophistiquée et à grande échelle de l'attaque DoS. Elle consiste à rendre un service, un serveur ou une infrastructure réseau indisponible en l'inondant de trafic provenant de multiples sources distinctes et géographiquement dispersées. 

## Explications détaillées
Contrairement au DoS simple, l'attaque DDoS utilise la puissance combinée de milliers, voire de millions de machines connectées à Internet. Ces machines, appelées "bots" ou "zombies", sont souvent des ordinateurs, des serveurs ou des objets connectés (IoT) infectés par des logiciels malveillants et contrôlés à distance par l'attaquant au sein d'un réseau appelé **Botnet**.

### Fonctionnement du Botnet et chaîne de commande
- **L'Attaquant** : Le cybercriminel qui planifie et lance l'attaque.
- **Command & Control (C2)** : Les serveurs centralisés ou décentralisés utilisés par l'attaquant pour envoyer des instructions aux machines infectées.
- **Les Bots (Zombies)** : Les systèmes compromis qui exécutent les ordres et envoient le trafic malveillant vers la victime.
- **La Victime** : L'infrastructure, le site web ou l'application ciblée par l'inondation.

```
[Attaquant] --> [Serveur C2] --> [Botnet (Des milliers d'IoT/PCs)] --> [Victime (Saturée)]
```

### Pourquoi le DDoS est-il redoutable ?
1. **Volume massif** : L'accumulation du trafic de chaque bot peut générer des flux allant de plusieurs gigabits par seconde (Gbps) à plusieurs térabits par seconde (Tbps).
2. **Difficulté de filtrage** : Le trafic malveillant est mélangé au trafic légitime. Bloquer une seule IP ne sert à rien, et bloquer toutes les IP attaquantes à la main est impossible en raison de leur grand nombre.
3. **Distribution mondiale** : Les paquets proviennent de pays différents, de fournisseurs d'accès internet (FAI) différents, rendant les politiques de filtrage géographique complexes et parfois inefficaces.

## Exemples concrets
- **Attaque par Botnet IoT** : En 2016, le botnet *Mirai*, constitué principalement de caméras IP et de routeurs domestiques compromis avec des mots de passe par défaut, a généré un trafic record de plus de 1 Tbps contre le fournisseur de DNS Dyn, paralysant une grande partie du web mondial.
- **Saturations applicatives distribuées** : Des milliers de bots envoient simultanément des requêtes de connexion légitimes à un site d'e-commerce pendant une période de soldes, le rendant inaccessible aux vrais acheteurs.

## Tableau de comparaison des volumes d'attaque
| Métrique | Attaque standard | Attaque d'envergure historique | Impact typique |
| :--- | :--- | :--- | :--- |
| **Débit volumétrique (Bande passante)** | 10 Gbps à 100 Gbps | 1.0 Tbps à 3.4 Tbps | Saturation complète des liens de transit FAI |
| **Débit de paquets (PPS)** | 1 à 10 Millions de PPS | 100+ Millions de PPS | Saturation des tables d'état des pare-feux et routeurs |
| **Débit applicatif (RPS)** | 10 000 à 50 000 RPS | 10+ Millions de RPS | Épuisement des pools de connexion des serveurs web |

## Avantages et limites de l'architecture DDoS (Perspective de l'attaquant)
### Avantages pour l'attaquant
- Forte résilience : L'arrêt de quelques bots n'impacte pas l'attaque.
- Anonymat élevé : L'attaquant est masqué derrière plusieurs couches de proxys et de serveurs C2.

### Limites pour l'attaquant
- Maintenance du botnet coûteuse et complexe.
- Détection des serveurs C2 par les chercheurs en cybersécurité entraînant le démantèlement du réseau.

## Bonnes pratiques de défense
1. **Recourir à un service de protection Cloud (Anycast)** : Distribuer le trafic sur des dizaines de centres de nettoyage (Scrubbing Centers) mondiaux.
2. **Surveillance comportementale** : Ne pas se fier uniquement aux listes d'IP, mais analyser le comportement du trafic réseau.
3. **Surdimensionnement des ressources (Overprovisioning)** : Avoir une capacité réseau supérieure aux besoins nominaux pour absorber les pics.

## Conclusion
Le DDoS est l'une des menaces les plus redoutables pour la disponibilité des systèmes informatiques. Sa nature distribuée exige des stratégies de défense coordonnées au niveau réseau global, impliquant des outils cloud avancés et des infrastructures de filtrage capables de séparer le trafic légitime du trafic malveillant en temps réel.