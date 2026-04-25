# Météo France - Analyse des Stations Météorologiques

## Description

Ce projet récupère et visualise les données des stations météorologiques françaises en utilisant l'API publique de Météo France. Il crée une base de données SQLite contenant les informations sur les stations de température et de précipitation, et génère des cartes interactives pour visualiser leur répartition géographique.

## Fonctionnalités

- **Récupération des données** : Extraction des informations des stations météorologiques via l'API Météo France
- **Base de données** : Stockage des données dans SQLite avec deux tables (température et précipitation)
- **Visualisation géographique** : Création de cartes interactives avec Folium
- **Comparaison** : Analyse des stations ayant uniquement des données de température ou de précipitation
- **Gestion des régions/départements** : Classification des stations par région et département français

## Structure du projet

### Fichiers principaux

- **`station2.0.py`** : Script principal pour récupérer les données des stations météorologiques via l'API Météo France
  - Crée et remplit la base de données SQLite
  - Gère les paramètres : température et précipitation
  - Inclut un système de gestion des quotas API

- **`carteStation.py`** : Génère une carte HTML (`triangles_map.html`) affichant toutes les stations
  - Marqueurs bleus pour les stations de température
  - Marqueurs rouges pour les stations de précipitation

- **`comparaison.py`** : Compare les stations et génère une carte des différences (`triangles_map2.html`)
  - Identifie les stations ayant uniquement des données de température
  - Identifie les stations ayant uniquement des données de précipitation

- **`regiondptsfrance.py`** : Dictionnaires contenant
  - Régions et leurs codes de département
  - Codes et noms complets des départements français

### Fichiers générés

- **`station.db`** : Base de données SQLite avec les tables :
  - `temperature` : Stations de température
  - `precipitation` : Stations de précipitation
  
- **`triangles_map.html`** : Carte interactive montrant toutes les stations
- **`triangles_map2.html`** : Carte interactive des stations avec données incomplètes

## Dépendances

```
requests
folium
scipy
numpy
sqlite3 (inclus dans Python)
```

## Installation

1. Clonez ou téléchargez le projet
2. Installez les dépendances :
```bash
pip install requests folium scipy numpy
```

## Configuration

Avant d'exécuter le projet, vous devez mettre à jour la clé API Météo France dans `station2.0.py` :

```python
api_key='votre_clé_api_ici'
```

Obtenez une clé API sur le [portail API Météo France](https://portail-api.meteofrance.fr/)

## Utilisation

1. **Récupérer les données** :
```bash
python station2.0.py
```
Cette commande crée la base de données et remplit les tables avec les données des stations.

2. **Générer la carte complète** :
```bash
python carteStation.py
```

3. **Générer la carte comparative** :
```bash
python comparaison.py
```

## Statistiques actuelles

D'après `docu.txt` :
- **Stations avec température** : 59 (marquées en bleu)
- **Stations avec précipitation** : 33 (marquées en rouge)
- **Total** : 92 stations

## Notes techniques

- Les cartes sont centrées sur la France métropolitaine (45.98°N, 3.32°E)
- Le zoom par défaut est fixé à 2 pour une vue d'ensemble
- La gestion des quotas API inclut une pause de 2 secondes en cas de dépassement
- Les positions des stations sont stockées en JSON dans la base de données

## Améliorations possibles

- [ ] Ajouter des graphiques temporels des données météorologiques
- [ ] Intégrer plus de paramètres (vitesse du vent, humidité, etc.)
- [ ] Créer une interface web pour consulter les données
- [ ] Ajouter des filtres par région/département
- [ ] Implémenter des statistiques et analyses avancées

## Licence

À déterminer

## Auteur

Milan
