#!/bin/sh

# Se déplacer dans le répertoire du projet front-end
cd /app/vacation_manager/theme/static_src

# Installer les dépendances Node.js et build assets
npm install
npm run build

# Revenir au répertoire racine de l'application Django
cd /app/vacation_manager

# Exécuter les migrations Django
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Démarrer Gunicorn
gunicorn --bind 0.0.0.0:8000 --workers 2 vacation_manager.wsgi:application