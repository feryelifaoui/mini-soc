# Rôles des équipes SOC en gestion d'incident DDoS

## Introduction
Définition des responsabilités et de l'organisation des analystes de sécurité lors d'une crise de déni de service.

## Fiche Technique
| Rôle | Responsabilité principale | Outil clé utilisé |
| :--- | :--- | :--- |
| **Analyste N1** | Détection précoce, Triage | Zabbix, Grafana, Alertes SIEM |
| **Analyste N2** | Investigation, Filtrage | tcpdump, consoles pare-feu / CDN |
| **Analyste N3** | Analyse avancée, Résilience | Outils de Threat Intelligence |
| **SOC Manager** | Direction de crise, Communication | Canaux de communication sécurisés (Teams/Signal) |

## Explications détaillées
### Principe et Fonctionnement
Un SOC (Security Operations Center) structuré attribue des responsabilités précises à ses membres pour éviter le chaos opérationnel en cas d'attaque. Chaque analyste doit connaître sa mission sur le bout des doigts lors du déclenchement du playbook DDoS.

### Structure opérationnelle du SOC en crise DDoS

#### Analyste N1 (Triage et Surveillance)
- Détecte le pic anormal de trafic réseau (PPS/BPS) ou la hausse soudaine des erreurs 5xx sur les consoles de monitoring.
- Valide que l'incident n'est pas une fausse alerte (ex: exclusion de travaux réseau planifiés).
- Escalade immédiatement l'incident au niveau 2 avec un rapport de synthèse initial.

#### Analyste N2 (Investigation et Mitigation)
- Analyse la structure des paquets (fichiers PCAP) pour identifier le vecteur d'attaque exact et les signatures de blocage.
- Met en œuvre les mesures de confinement initiales (ex: écriture de règles de pare-feu, activation de WAF rules).
- Coordonne techniquement les actions avec les partenaires externes (hébergeur, FAI, CDN).

#### Analyste N3 (Expertise et Gouvernance)
- Gère les cas complexes où l'attaque DDoS mute fréquemment pour contourner les protections.
- Valide les modifications majeures d'infrastructure (ex: déviation complète du trafic réseau).
- Assure le rôle de conseiller technique pour le SOC Manager et la cellule de crise générale.

#### SOC Manager / Incident Commander
- Dirige la cellule de crise et coordonne la réponse globale.
- Communique l'avancement de la résolution à la direction générale et aux équipes de communication.
- Libère les ressources nécessaires et prend les décisions à fort impact business (ex: activation d'un Null Routing).

### Bonnes pratiques
1. Définir une matrice RACI (Réalisateur, Approbateur, Consulté, Informé) pour chaque étape du playbook DDoS.
2. S'assurer que les rôles de "Responsable Technique" et "Responsable de la Communication" sont attribués à des personnes différentes pour éviter la surcharge.

## Bonnes pratiques de cybersécurité
1. Établir des procédures écrites et testées avant la crise.
2. Coordonner les actions de communication et techniques.
3. Rédiger systématiquement des rapports post-incident pour améliorer la résilience.

## Conclusion
La réponse aux incidents DDoS ne s'improvise pas. Elle nécessite une organisation structurée (rôles SOC), une méthodologie éprouvée (cycle NIST) et des plans de secours (PCA/PRA) clairs pour maintenir la continuité d'activité de l'entreprise sous toutes les circonstances.
