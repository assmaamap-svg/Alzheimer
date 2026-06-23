# Vue d'ensemble 

Ce dépôt contient l’ensemble des travaux réalisés dans le cadre de la soutenance Développeur en Science des Données.
Le projet porte sur la prédiction précoce du risque de développer la maladie d’Alzheimer, en exploitant les données médicales ADNI et un pipeline complet allant de la donnée brute jusqu’au modèle déployé.

# Problèmatique
Comment exploiter les données médicales et les techniques de Machine Learning pour prédire précocement le risque de développer la maladie d’Alzheimer, afin d’aider les médecins à la décision et d’améliorer la prise en charge des patients ?

# Concepteurs
Bruce VIGNOLLES  
Assmaa ABDELMOUMNI  
Magalie CESARINI  

# Structure du dépôt
```bash
Code
├── architecture/            # Schémas d’architecture (pipeline, datalake)
│
├── data/                    # Données ADNI (extraits anonymisés)
│   ├── raw/                 # Données brutes
│   │   └── IRM/             # Scans IRM
│   └── processed/           # Données nettoyées / features
│
├── etl/                     # Pipelines d’ingestion & transformation
│   ├── knime/               # Workflows KNIME
│   └── powerbi/             # Power BI (schéma en étoile)
│
├── industrialisation/       # Backend FastAPI + frontend Streamlit
│   ├── src/                 # Pipelines + logique métier (préprocessing, training)
│   ├── artifacts/           # Models / Metrics exportés pour l'API
│   ├── backend/             # Code backend (routes FastAPI)
│   ├── frontend/            # Code Streamlit (UI)
│   └── requirements.txt     # Dépendances API
│
├── ml/                      # Machine Learning tabulaire
│   ├── notebooks/           # EDA, préprocessing, modèles ML
│   ├── models/              # Modèles ML
│   └── src/                 # Scripts ML (prépocessing, training)
│
├── dl/                      # Deep Learning (IRM)
│   ├── notebooks/           # CNN, prétraitement images
│   └── models/              # Modèles DL              
│
├── docs/                    # Documentation projet
│   ├── pia/                 # Rapport PIA RGPD
│   └── fiche_projet/        # Cadrage
│
├── powerbi/                 # Dashboard
│
└── README.md                # Présentation du projet
```


# Travaux effectués
## 1. Collecte des données – ADNI
https://ida.loni.usc.edu/explore/jsp/search_v2/search.jsp?project=ADNI 

Les données proviennent de 10 tables médicales intégrées dans un datalake :

    MMSE : Tests cognitifs

    ADAS : Tests neuropsychologiques

    CDR : Niveau de démence

    PHYSICAL : Mesures vitales

    UCSFFSX7 : Biomarqueurs IRM (hippocampe, cortex…)

    PTDEMOG : Données démographiques

    FAMHXPAR : Antécédents familiaux

    MEDHIST : Antécédents médicaux

    INITHEALTH : Santé initiale

    DXSUM : Diagnostics (labels)

## 2. Ingestion & Stockage
Outils utilisés

    KNIME : ETL open‑source pour automatiser l’ingestion

    Python : nettoyage, feature engineering, scripts reproductibles

    Supabase (PostgreSQL + S3) : stockage structuré + stockage objets
    https://supabase.com/dashboard/project/chsezchtwttnlyyiwovj/storage/files/buckets/DataLakeAlzheimer

Pourquoi ces choix ?

    KNIME → visuel, reproductible, idéal pour un pipeline ETL pédagogique

    Python → flexibilité, ML, DL, automatisation

    Supabase → gratuit jusqu’à 500 Mo, API REST auto, parfait pour un POC


## 3. Analyse exploratoire (EDA)

Analyse statistique et visuelle :

    Répartition des diagnostics

    Corrélations entre variables

    Analyse des biomarqueurs IRM

    Étude des tests cognitifs (MMSE, ADAS, CDR)

    Détection des valeurs manquantes


## 4. Préprocessing

    Fusion des 10 tables

    Nettoyage & imputation

    Encodage des variables catégorielles

    Normalisation si nécessaire

    Split train/test stratifié

## 5. Machine Learning
Modèle principal : RandomForestClassifier

    Gère très bien les données hétérogènes

    Robuste au bruit et aux valeurs manquantes

    Interprétable via feature importance

    Performant sur des datasets médicaux de taille moyenne

    Pas de normalisation obligatoire

Excellent compromis entre performance et interprétabilité, indispensable en santé.
## 6. Métriques – Pourquoi F1-score ?

En médecine, les classes sont déséquilibrées.

    Accuracy → trompeuse

    Recall → important pour ne pas rater un malade

    Precision → important pour éviter les faux positifs

F1-score = meilleur compromis entre précision et rappel.
## 7. Deep Learning sur IRM

Utilisation de CNN pour analyser les images IRM (atrophie hippocampique).

    Prétraitement des images

    Modèle CNN (TensorFlow / Keras)

    Classification Alzheimer / Sain

## 8. Visualisation – Power BI

Création de dashboards interactifs :

    évolution des scores cognitifs

    segmentation des patients

    importance des variables du modèle

Permet une interprétation clinique des résultats.
## 9. Industrialisation

Déploiement du modèle via :

    FastAPI (API REST)

    Docker (reproductibilité)

    Render (hébergement gratuit)


 https://alzheimer-frontend-wn2w.onrender.com  

Pipeline automatisé sans intervention manuelle répétée.
## 10. Gestion de projet

    Jira : backlog, user stories, sprints

    Confluence : documentation technique, schémas, décisions


## Conclusion

Ce projet démontre la maîtrise complète du cycle de vie d’un projet data :

    Collecte

    ETL

    Stockage

    EDA

    Préprocessing

    Machine Learning

    Deep Learning

    Visualisation

    Déploiement

    Documentation

    Gestion de projet
