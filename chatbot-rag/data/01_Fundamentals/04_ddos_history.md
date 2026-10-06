# Historique des attaques DDoS

## Introduction
Les attaques DDoS n'ont cessé d'évoluer depuis l'émergence d'Internet. D'abord simples farces d'étudiants ou démonstrations techniques, elles sont devenues des armes géopolitiques et des outils d'extorsion industrielle hautement sophistiqués. Cette évolution est intimement liée à l'augmentation de la bande passante globale et à la prolifération des objets connectés vulnérables.

## Explications détaillées

### 1. Les origines (Années 1990 - 2000)
- **1999 - L'outil Trinoo** : L'un des premiers outils DDoS documentés. Il permettait à un attaquant de coordonner plusieurs machines compromises pour inonder une cible de paquets UDP.
- **Février 2000 - L'attaque de "MafiaBoy"** : Un lycéen canadien de 15 ans utilise les outils *Trinoo* et *TFN* (Tribe Flood Network) pour paralyser les plus grands sites de l'époque, notamment Yahoo! (alors le premier moteur de recherche), Amazon, eBay et CNN. Cette attaque a révélé la vulnérabilité intrinsèque de l'architecture d'Internet au grand public et aux gouvernements.

### 2. L'ère de la politisation et du hacktivisme (2007 - 2012)
- **2007 - Cyberattaques contre l'Estonie** : Suite à des tensions diplomatiques avec la Russie concernant le déplacement d'un monument soviétique, l'Estonie subit une vague d'attaques DDoS massives ciblant ses parlements, banques, ministères et médias. C'est l'un des premiers cas documentés de guerre cybernétique impliquant le DDoS à l'échelle d'un État.
- **2010 - Opération Payback (Anonymous)** : Le collectif d'hacktivistes Anonymous lance des attaques DDoS contre Visa, MasterCard et PayPal à l'aide de l'outil LOIC (*Low Orbit Ion Cannon*). LOIC permettait à des volontaires de prêter volontairement leur bande passante pour surcharger les cibles en soutien à WikiLeaks.

### 3. L'émergence des Botnets IoT et l'ère du Térabit (2016 - Présent)
- **2016 - Le Botnet Mirai** : Mirai a révolutionné le DDoS en exploitant la sécurité inexistante des objets connectés (IoT) comme les caméras IP et les routeurs. En scannant Internet à la recherche de ports Telnet ouverts avec des identifiants par défaut, Mirai a infecté des centaines de milliers de machines. Il a généré une attaque de 1.2 Tbps contre le fournisseur de DNS Dyn, rendant indisponibles des sites comme Twitter, Netflix et Spotify.
- **2018 - L'attaque contre GitHub (1.35 Tbps)** : Cette attaque a utilisé une technique d'amplification via des serveurs *Memcached* exposés sur Internet, sans nécessiter de botnet traditionnel. Le facteur d'amplification était de 50 000, un record technique.
- **2022/2023 - Les attaques records à plus de 3 Tbps** : Cloudflare et Google ont rapporté des attaques applicatives (HTTP/2 Rapid Reset) et volumétriques dépassant les 3 Tbps et des centaines de millions de requêtes par seconde, menées par des botnets basés sur des serveurs virtuels (VPS) puissants plutôt que de simples objets IoT.

## Frise chronologique des attaques marquantes
| Année | Cible principale | Type d'attaque / Outil | Volume / Particularité |
| :--- | :--- | :--- | :--- |
| **2000** | Yahoo!, Amazon, eBay | UDP/ICMP Flood (MafiaBoy) | Paralysie du web commercial naissant |
| **2007** | Infrastructures de l'Estonie | Botnets de spam et ping floods | Première cyberguerre d'envergure nationale |
| **2010** | MasterCard, PayPal | LOIC (Anonymous) | Hacktivisme distribué basé sur le volontariat |
| **2016** | Dyn (DNS Provider) | Botnet IoT Mirai | > 1.2 Tbps - Saturation de l'infrastructure DNS |
| **2018** | GitHub | Amplification Memcached | 1.35 Tbps - Utilisation de serveurs de cache |
| **2023** | Acteurs Cloud majeurs | HTTP/2 Rapid Reset | 398 Millions de Requêtes par seconde (RPS) |

## Enseignements de l'histoire
- **La course aux armements** : À mesure que les réseaux augmentent leur capacité, les attaquants découvrent de nouvelles techniques de réflexion et d'amplification pour multiplier leur force de frappe.
- **La sécurité IoT est cruciale** : La prolifération d'objets connectés mal protégés fournit aux attaquants une armée gratuite de bots.
- **La transition vers le Cloud** : Les entreprises ne peuvent plus se défendre seules avec des équipements sur site (On-Premise) ; la protection doit être déportée dans le cloud.

## Conclusion
L'histoire du DDoS montre que cette menace n'est pas statique. D'une simple saturation de bande passante TCP/UDP dans les années 2000, nous sommes passés à des attaques applicatives complexes tirant parti des failles de protocoles modernes comme HTTP/2. La veille technologique et l'adaptation constante des défenses sont indispensables.