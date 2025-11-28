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


docker stop $(docker ps -aq) && docker rm -f $(docker ps -aq) && docker volume rm $(docker volume ls -q) && docker network prune -f -f && docker rmi -f $(docker images -q)

itnetwork@florent ~/project/vacation-manager/docker/production [±master S:1 U:8 ?:40 ✗] docker compose -f docker-compose-production.yml up
