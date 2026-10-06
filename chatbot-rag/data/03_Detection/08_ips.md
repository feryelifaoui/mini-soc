# IPS (Intrusion Prevention System)

## Introduction
Système actif positionné en ligne sur le réseau, capable de détecter et de bloquer immédiatement le trafic malveillant.

## Fiche Technique
| Critère | Description |
| :--- | :--- |
| **Mode de connexion** | En ligne (Inline / Bridge) |
| **Action** | Détection + Blocage automatique (Drop, Reset) |
| **Risque réseau** | Élevé (coupure réseau potentielle, faux positifs) |
| **Exemples** | Cisco Firepower, Suricata (en mode IPS) |

## Explications détaillées
### Principe et Fonctionnement
Un IPS (Intrusion Prevention System) est une évolution de l'IDS. Il est positionné "en ligne" (Inline), ce qui signifie que tout le trafic réseau traverse physiquement l'équipement. L'IPS analyse le trafic en temps réel et dispose de la capacité d'interagir immédiatement avec le flux. S'il détecte une signature d'attaque DDoS (ex. un volume anormal de requêtes HTTP GET malformées), l'IPS jette immédiatement les paquets malveillants (*drop*), réinitialise la connexion TCP (*TCP Reset*) ou modifie les règles du pare-feu à la volée.

### Avantages et Limites
- **Avantages** :
  - Protection active et blocage immédiat des menaces en temps réel.
  - Automatisation de la réponse aux incidents de premier niveau.
- **Limites** :
  - Point de défaillance unique (Single Point of Failure) : si l'IPS subit une panne matérielle ou logicielle, le réseau peut être coupé.
  - Risque de blocage d'utilisateurs légitimes en cas de faux positifs (impact business direct).

### Bonnes pratiques
1. Configurer l'IPS avec une fonction de "Bypass matériel" (Bypass Card) pour assurer la continuité du trafic en cas de panne de l'équipement.
2. Tester longuement les nouvelles signatures en mode "IDS/Alerte" avant de les passer en mode "IPS/Blocage".

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
