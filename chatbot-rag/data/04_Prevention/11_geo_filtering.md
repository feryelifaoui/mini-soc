# Filtrage géographique (Geo-blocking)

## Introduction
Technique consistant à bloquer ou à autoriser le trafic réseau en fonction du pays d'origine de l'adresse IP du client.

## Fiche Technique
| Action Géographique | Effet sur le trafic | Risque de faux positifs |
| :--- | :--- | :--- |
| **Block (Blocage pur)** | Rejet immédiat de la connexion | Élevé |
| **Challenge (CAPTCHA/JS)** | Vérification de la légitimité du client | Faible |
| **Allow (Autorisation)** | Trafic autorisé à se connecter | Aucun |

## Explications détaillées
### Principe et Fonctionnement
Le filtrage géographique (ou Geo-blocking) s'appuie sur des bases de données IP-to-Location (ex: MaxMind GeoIP) pour associer chaque adresse IP publique entrante à un pays ou une région géographique spécifique. Le pare-feu, le WAF ou le CDN utilise cette information pour appliquer des politiques d'accès différenciées. Par exemple, une entreprise publique locale française qui ne propose ses services qu'à des clients nationaux peut décider de bloquer tout trafic provenant d'autres continents.

### Rôle dans la prévention DDoS
- **Réduction drastique de la surface d'attaque** : Si un botnet mondial lance une attaque DDoS et que 80% des bots sont situés dans des pays où l'entreprise n'a pas d'activité commerciale, le geo-blocking permet d'éliminer immédiatement ces flux suspects à la frontière réseau.
- **Préservation des ressources** : Permet de concentrer la bande passante et la puissance de calcul sur les utilisateurs des régions cibles.

### Avantages et Limites
- **Avantages** :
  - Simple et rapide à mettre en œuvre sur un WAF ou un CDN.
  - Efficacité immédiate contre les botnets basés dans des régions géographiques spécifiques.
- **Limites** :
  - Inefficace si les bots de l'attaquant sont situés dans le même pays que les utilisateurs légitimes.
  - Risque de bloquer des clients légitimes en déplacement à l'étranger ou utilisant des VPN commerciaux localisés dans d'autres pays.

### Bonnes pratiques
1. Plutôt que de bloquer purement et simplement, appliquer des défis JavaScript ou CAPTCHA (mode "Challenge") pour le trafic provenant de pays hors cible commerciale.
2. Maintenir la base de données de géolocalisation IP à jour régulièrement pour éviter les erreurs d'adressage.

## Bonnes pratiques de cybersécurité
1. Appliquer une défense multi-couches.
2. Minimiser la surface d'exposition internet.
3. Concevoir des systèmes redondants et résilients.

## Conclusion
La prévention DDoS est un processus continu qui s'intègre dès la conception de l'architecture informatique. Une combinaison équilibrée de pare-feux, WAF, CDN et de haute disponibilité permet de réduire drastiquement l'impact potentiel des attaques.
