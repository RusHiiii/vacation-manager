# Vacation Manager

Florent Damiens - 2025 / 2026

## Contexte

Vacation Manager est une application web de gestion des congés. Elle permet de suivre les jours de congés acquis, utilisés et restants sur une période de deux ans (année N et N+1).

## Features

Il y a plusieurs fonctionnalités sur le projet :

- **Suivi des congés** : Visualisation mensuelle des congés cumulés, utilisés et restants
- **Paramétrage personnalisé** : Configuration du solde initial, des RTT et des congés mensuels
- **Demande de congés** : Formulaire de saisie des jours pris par mois
- **Gestion multi-année** : Suivi sur l'année en cours et l'année suivante
- **Authentification** : Système de connexion sécurisé par utilisateur

_Note : L'interface d'administration est celle de Django._

## Technologies

| Catégorie | Technologie | Version |
|-----------|-------------|---------|
| **Backend** | Python | 3.11+ |
| | Django | 5.2 |
| **Frontend** | Tailwind CSS | 4.x |
| | django-tailwind | 4.2 |
| | Node.js | 20.x |
| **Base de données** | PostgreSQL | 15+ |
| **Conteneurisation** | Docker / Docker Compose | - |
| **Environnement local** | Devenv (Nix) | - |

## Installation

### Prérequis

- Git
- Docker et Docker Compose (production)
- Devenv / Nix (local)

### Développement local avec Devenv

1. **Cloner le projet**

```bash
git clone https://github.com/rushiiii/vacation-manager.git
cd vacation-manager
```

2. **Installer Devenv** (si non installé)

```bash
sh <(curl -L https://devenv.sh/install.sh)
```

3. **Lancer l'environnement**

```bash
devenv up
```

Cette commande démarre automatiquement :
- PostgreSQL sur le port 5432
- Le serveur Django sur http://localhost:8000
- Le watcher Tailwind CSS

Toute la configuration est dans le fichier devenv.nix, il y a également les variables d'environnements.

⚠️ Il est possible que si on souhaite tester avec docker, les variables d'environnement spécifier dans le fichier devenv.nix rentre en conflit et bypass toutes les variables d'environnements que nous spécifions dans les fichiers .env standards.
Pour éviter ça il faut lancer la commande suivante `direnv deny .`

4. **Appliquer les migrations** (dans un autre terminal)

```bash
devenv shell
python vacation_manager/manage.py migrate
```

5. **Créer un superutilisateur**

```bash
python vacation_manager/manage.py createsuperuser
```

6. **Initialiser les données de congés**

```bash
python vacation_manager/manage.py initialize_holiday
```

#### Variables d'environnement (Devenv)

Les variables sont configurées automatiquement dans `devenv.nix` :

| Variable | Valeur par défaut |
|----------|-------------------|
| `DJANGO_DEBUG` | `True` |
| `DATABASE_USERNAME` | `vacation_manager` |
| `DATABASE_PASSWORD` | `pass` |
| `DATABASE_HOST` | `127.0.0.1` |
| `DATABASE_PORT` | `5432` |

### Production avec Docker

1. **Cloner le projet**

```bash
git clone https://github.com/rushiiii/vacation-manager.git
cd vacation-manager
```

2. **Configurer les variables d'environnement**

Créer un fichier `.env` à la racine :

```bash
DJANGO_SECRET_KEY=votre-cle-secrete-complexe
DJANGO_DEBUG=False
DJANGO_LOGLEVEL=info
DJANGO_ALLOWED_HOSTS=localhost

DATABASE_NAME=vacation_manager
DATABASE_USERNAME=vacation_manager
DATABASE_PASSWORD=mot-de-passe-securise
DATABASE_HOST=db
DATABASE_PORT=5432
```

3. **Construire et démarrer les conteneurs**

```bash
docker compose up -d --build
```

4. **Appliquer les migrations**

```bash
docker compose exec django-web python vacation_manager/manage.py migrate
```

5. **Créer un superutilisateur**

```bash
docker compose exec django-web python vacation_manager/manage.py createsuperuser
```

6. **Initialiser les données**

```bash
docker compose exec django-web python vacation_manager/manage.py initialize_holiday
```

L'application est accessible sur http://localhost:8080

#### Commandes Docker utiles

```bash
# Voir les logs
docker compose logs -f

# Arrêter les conteneurs
docker compose down

# Reconstruire complètement (avec suppression des volumes)
docker compose down --volumes
docker compose up --build --force-recreate

# Accéder au shell Django
docker compose exec django-web bash
```
