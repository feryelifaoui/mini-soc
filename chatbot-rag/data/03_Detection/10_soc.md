# SOC (Security Operations Center)

## Introduction
Le centre opérationnel de sécurité composé d'analystes chargés de surveiller, détecter et répondre aux incidents de sécurité 24h/24 et 7j/7.

## Fiche Technique
| Composant | Rôle du SOC |
| :--- | :--- |
| **Humains** | Analystes qualifiés travaillant en rotation (24/7) |
| **Processus** | Playbooks d'atténuation DDoS, règles d'escalade, PCA/PRA |
| **Technologies** | SIEM, IDS/IPS, WAF, Consoles Cloud (Cloudflare, Akamai) |

## Explications détaillées
### Principe et Fonctionnement
Le SOC (Security Operations Center) est une entité organisationnelle (interne ou externalisée) composée d'experts en cybersécurité (analystes N1, N2, N3). Le rôle du SOC est de surveiller en permanence les alertes générées par les outils de détection (notamment le SIEM) pour qualifier les incidents de sécurité. En cas d'attaque DDoS, les analystes du SOC activent le plan de réponse à incident, collaborent avec les équipes réseau pour appliquer des règles de blocage (mitigation), et coordonnent la communication technique avec l'hébergeur ou le FAI.

### Rôles clés dans le SOC face à un DDoS
- **Analyste N1 (Triage)** : Détecte l'alerte de pic de trafic réseau, qualifie la nature de l'attaque et escalade l'alerte au niveau supérieur.
- **Analyste N2 (Incident Response)** : Analyse l'attaque (vecteurs, ports, volume), définit les règles de filtrage temporaires à appliquer sur le WAF/pare-feu ou active le service de redirection cloud.
- **Analyste N3 / SOC Manager** : Dirige la cellule de crise, coordonne les actions avec les partenaires externes (FAI, éditeurs de sécurité) et rédige le rapport d'incident post-mortem.

### Bonnes pratiques
1. Établir des playbooks (procédures écrites) clairs et testés pour chaque type d'attaque DDoS.
2. Réaliser des exercices réguliers de simulation d'attaque DDoS pour tester la réactivité du SOC.

## Bonnes pratiques de cybersécurité
1. Surveiller les indicateurs en temps réel.
2. Corréler les logs réseau et applicatifs.
3. Maintenir à jour les profils de trafic normaux.

## Conclusion
La détection est la clé de voûte de la défense DDoS. Une détection rapide et précise permet d'activer les mécanismes de mitigation appropriés avant que l'infrastructure ne devienne indisponible.
