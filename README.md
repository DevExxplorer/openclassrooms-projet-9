# Openclassrooms: Développez une application Web en utilisant Django

## Installation
***
Activez l'environnement et installez les packages à l'aide du fichier requirements.txt :
```
python -m venv <environment name>
source <environment name>/bin/activate
pip install -r requirements.txt
```

## Utilisation
***
Pour lancer l'application:
```bash
cd litrevu && python manage.py runserver
```

Pour lancer la compilation des fichiers sass en css:
```bash
cd litrevu &&  python manage.py sass app/static/app/scss/ app/static/app/css/ --watch
```