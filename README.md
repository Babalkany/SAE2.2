# SAE C2 Bastien B Tom L

Logiciel d'empilement d'image pour la SAE C2 de BUT2 APP pour **Bastien BRUNEL** & **Tom LECLERCQ**.
dernière version daté de 13/12/2022

## Installation

Nous avons codé la saé via **python 3.10.5** et nous vous conseillons de faire de même
Pour exécute le programme il faut utiliser les bibliothèques suivantes:
Installation avec [pip](https://pip.pypa.io/en/stable/)

 **1. Numpy**
Nous avons travaillé avec la **version 1.22.2**
Vous pouvez Installer Numpy avec :

```bash
pip install numpy
```

 **2. Matplotlib**
Nous avons travaillé avec la **version 3.6.2**
Vous pouvez installer MatPlotLib avec :

```bash
pip install matplotlib
```

 **3. Astropy**
Nous avons travaillé avec la **version 5.1.1**
Vous pouvez installer Astropy avec :

```bash
pip install astropy
```

**4. PyQt5**
Nous avons travaillé avec la **version 5.15.7** de PyQt5
Vous pouvez l'installer avec :

```bash
pip install pyQt5
```

## Utilisation

Pour exécuter notre programme il faut simplement exécuter le fichier ``main.py`` depuis un IDE ou via la commande :

```bash
 py main.py
```

## Résumé des fonctionnalités

- **Charger les images en .fits** **(en niveau de gris)** dans le code grâce a une interface graphique en les sélectionnant dans l'onglet qui s'affiche.
- **Empilement par moyenne** en cliquant sur le bouton correspondant en bas de la fenêtre PyQt5.
- **Empilement par médiane** en cliquant sur le bouton correspondant en bas de la fenêtre PyQt5.
- ~~Empilement avec rejet des *outliers* **(en Cours)** de manière automatique au lancement du code et avec les 2 méthodes~~
