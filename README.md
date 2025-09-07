# Gestionnaire pour les vacances

## Installation

```bash
down les volumes
docker compose down --volumes

force recreate
docker compose up --build --force-recreate
```

## Lancer les migrations

```python 
python vacation_manager/manage.py migrate
```

```
DJANGO_SECRET_KEY=XXX
DEBUG=True
DJANGO_LOGLEVEL=info
DJANGO_ALLOWED_HOSTS=localhost

DATABASE_NAME=vacation_manager
DATABASE_USERNAME=vacation_manager
DATABASE_PASSWORD=pass
DATABASE_HOST=db
DATABASE_PORT=5432
```