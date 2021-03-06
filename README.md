[![Stories in Ready](https://badge.waffle.io/AESSUQAM/EnceFAL.png?label=ready&title=Ready)](https://waffle.io/AESSUQAM/EnceFAL)
[![Build Status](https://travis-ci.org/AESSUQAM/EnceFAL.svg?branch=develop)](https://travis-ci.org/AESSUQAM/EnceFAL)
[![Coverage Status](https://coveralls.io/repos/github/AESSUQAM/EnceFAL/badge.svg?branch=develop)](https://coveralls.io/github/AESSUQAM/EnceFAL?branch=develop)
# EnceFAL 

EnceFAL est un projet Django, qui vise à faciliter la gestion de foires aux livres usagés

## Installation

```
# 1. cloner le repo
git clone https://github.com/AESSUQAM/EnceFAL.git
cd EnceFAL

# 2. Créer un environnement python virtuel
sudo apt-get install virtualenv
virtualenv py_env

# 3. Installer setuptools Ver >=21.0.0 et buildout avec easy install
sudo py_env/bin/easy_install -U setuptools
sudo py_env/bin/easy_install zc.buildout

## 3.1 installer setuptools et buildout avec pip (Optionel, si easy_install n'est pas installé)
sudo py_env/bin/pip install --upgrade setuptools
sudo py_env/bin/pip install zc.buildout

### 3.2 Au cas où ni pip, ni easy_install n'est installé
http://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/

# 4. Setter les dépendances
sudo py_env/bin/buildout

# 5. Modifier les settings pour développement
cd project
cp conf.py.edit conf.py
# dans conf.py, editer les configs de la bd locale

# 6. créer la bd locale.
cd ..
bin/django makemigrations
bin/django migrate --fake-initial

# 7. Lancer le serveur !
bin/django runserver
```

#### _**Lancer les tests**_

```
# Si pas déjà dans le dossier du projet
cd EnceFAL

# On lance la suite de test de django
bin/django test
```
