# Rapport d'Analyse : Capacité et Performance des Centres de Service

Ce projet documente la transformation et l'analyse statistique du réseau des centres de service. L'étude se concentre sur la corrélation entre les infrastructures physiques, les amplitudes horaires et la capacité de traitement journalière.
 ## Table des Matières

    Architecture du Dataset

    Méthodologie de Transformation

    Environnement Technique

    Analyse de Corrélation et Linéarité

    Synthèse des Résultats

 ## Architecture du Dataset

Les données sources contiennent les caractéristiques de deux types de structures :

    Centres Principaux : Hubs stratégiques à haut volume.

    Centres Secondaires : Unités de proximité.

 ## Variables clés :

    personnel_capacite_jour : Volume maximum de traitement.

    nombre_guichets : Nombre de postes de travail physiques.

    heures_ouverture : Plage horaire de service.

    date_ouverture : Date de mise en service initiale.

## Méthodologie de Transformation

Pour obtenir une analyse quantitative exploitable, les étapes suivantes ont été appliquées :

    Ingénierie de variables (Feature Engineering) :

        Total Heures : Conversion des plages horaires (ex: 07:30-17:30) en valeurs numériques (ex: 10.0).

        Ancienneté : Calcul du nombre d'années d'activité par soustraction entre l'année actuelle et l'année de date_ouverture.

    Nettoyage du DataFrame :

        Utilisation de la fonction .drop() avec le paramètre axis=1.

        Suppression des colonnes textuelles d'origine (heures_ouverture, date_ouverture) pour ne conserver que les indicateurs calculés.

## Environnement Technique

L'analyse repose sur la pile technologique Python Data Science :

    Pandas : Manipulation matricielle et nettoyage.

    NumPy : Opérations mathématiques sur les vecteurs.

    Seaborn & Matplotlib : Génération des visualisations avancées (Heatmaps et Pairplots).


# Synthèse des Résultats

    **Standardisation** : La linéarité des données prouve que les processus opérationnels sont hautement standardisés sur l'ensemble du territoire.

    **Segmentation** : Le réseau est binaire. Les centres "Principaux" (bleu) et "Secondaires" (orange) forment deux clusters distincts sans zone intermédiaire, reflétant une politique de déploiement par paliers.

    **Optimisation** : Pour augmenter la capacité globale, l'extension des horaires de service des centres secondaires est mathématiquement plus efficace que le simple vieillissement du parc de centres actuels.

