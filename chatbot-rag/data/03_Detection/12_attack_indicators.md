# Indicateurs d'une attaque DDoS (IOCs)

## Introduction
Signaux d'alerte et indices techniques permettant d'identifier de manière certaine qu'une infrastructure subit une attaque DDoS.

## Fiche Technique
| Indicateur | Cause probable | Type de DDoS associé |
| :--- | :--- | :--- |
| **Trafic UDP 123 massif** | Réflexion/Amplification NTP | Volumétrique |
| **Connexions à l'état SYN_RECV** | Inondation de paquets SYN | Protocolaire |
| **Erreurs HTTP 504 en boucle** | Serveurs backend saturés | Applicatif |
| **Requêtes NXDOMAIN DNS** | Inondation de résolutions aléatoires | Applicatif DNS |

## Explications détaillées
### Principe et Fonctionnement
Reconnaître rapidement une attaque DDoS évite de perdre du temps à chercher des pannes matérielles ou des bugs applicatifs. Les analystes réseau s'appuient sur un ensemble d'indicateurs de compromission (IOCs) et d'anomalies de performance pour qualifier l'attaque.

### Liste des principaux indicateurs d'attaque
1. **La latence du ping s'envole** : Le temps de réponse vers les serveurs passe de quelques millisecondes à plusieurs secondes, avec un taux important de paquets perdus.
2. **Le trafic entrant est asymétrique** : Le débit descendant (Inbound) sur l'interface réseau publique est à 100% de sa capacité, tandis que le débit montant (Outbound) reste normal ou s'effondre.
3. **Le CPU des équipements de sécurité sature** : Les pare-feux ne répondent plus aux consoles d'administration en raison d'une surcharge processeur.
4. **Les serveurs web retournent des erreurs de timeout** (502/504) ou "Connexion refusée", bien que la machine physique soit allumée.
5. **Concentration géographique suspecte** : Les logs web montrent une hausse spectaculaire de requêtes provenant de pays inhabituels pour l'activité de l'entreprise.

### Bonnes pratiques
1. Créer une check-list rapide des indicateurs DDoS pour les équipes d'astreinte informatique.
2. Automatiser l'envoi de rapports d'anomalies en cas de détection simultanée de 3 indicateurs clés.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
