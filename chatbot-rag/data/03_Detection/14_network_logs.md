# Journaux réseau (Network Logs)

## Introduction
Exploitation des logs de pare-feux, serveurs web et DNS pour identifier l'origine et la structure d'une attaque.

## Fiche Technique
| Source de log | Informations clés fournies | Format standard |
| :--- | :--- | :--- |
| **Nginx Access Log** | IP, Date, Request URI, HTTP Status, User-Agent | NCSA Common/Combined |
| **PfSense/Firewall Log** | Interface, Action (Pass/Block), Source IP, Dest IP, Protocol | Syslog CSV |
| **BIND Query Log** | Client IP, Query Name, Query Type (A, AAAA, ANY) | BIND format |

## Explications détaillées
### Principe et Fonctionnement
Les journaux réseau (logs) constituent la mémoire historique des événements de l'infrastructure. Lors d'une phase de détection ou d'investigation post-incident, l'analyse minutieuse de ces logs permet d'extraire la signature exacte de l'attaque.

### Les différentes sources de logs
- **Logs de pare-feu** : Enregistrent les connexions acceptées et bloquées, les adresses IP sources/destinations, et les ports. Utiles pour identifier les pics de connexions bloquées par IP.
- **Logs d'accès du serveur web (Access Logs)** : Enregistrent chaque requête HTTP reçue (Adresse IP client, Date/Heure, Méthode GET/POST, URL demandée, Code de retour HTTP, User-Agent). Permettent d'isoler les signatures des bots applicatifs.
- **Logs de serveurs DNS (Query Logs)** : Contiennent l'historique des requêtes de résolution reçues. Essentiels pour détecter un DNS Query Flood.

### Bonnes pratiques
1. Centraliser les logs sur un serveur Syslog externe ou dans le SIEM pour éviter qu'ils ne soient perdus si le serveur web ciblé crashe.
2. Configurer la rotation automatique des journaux pour éviter que l'espace disque du serveur ne se sature pendant une attaque générant des gigaoctets de logs en quelques minutes.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
