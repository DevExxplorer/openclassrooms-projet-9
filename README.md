# Openclassrooms: Développez une application Web en utilisant Django

## Installation
***
Activez l'environnement et installez les packages à l'aide du fichier requirements.txt :
```
git clone git@github.com:DevExxplorer/openclassrooms-projet-9.git
cd openclassrooms-projet-9
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Utilisation
***
Pour lancer l'application (premiere fois):
```bash
cd litrevu && python manage.py migrate && python manage.py runserver
```

Pour lancer l'application:
```bash
cd litrevu && python manage.py runserver
```


Pour lancer la compilation des fichiers sass en css:
```bash
cd litrevu &&  python manage.py sass app/static/app/scss/ app/static/app/css/ --watch
```