# Image Python
FROM python:3.13-slim

# Empêche Python de créer des .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dossier de travail
WORKDIR /app

# Dépendances système minimales
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de dépendances
COPY pyproject.toml ./

# Installer pip + dépendances
RUN pip install --upgrade pip \
    && pip install .

# Copier le reste du projet
COPY . .

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Port exposé (Render / Railway utilisent $PORT)
EXPOSE 8000

# Lancer Django avec Gunicorn
CMD gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000}
