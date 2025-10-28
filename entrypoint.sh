#!/bin/bash

echo "🚀 Lancement du conteneur Django..."

sleep 5

echo "📦 Application des migrations..."
python manage.py migrate --noinput

echo "📤 Chargement des fixtures..."
python manage.py loaddata category/fixtures/categories.json || echo "⚠️ Fixtures Category déjà chargées ou introuvables."
python manage.py loaddata event/fixtures/event.json || echo "⚠️ Fixtures Event déjà chargées ou introuvables."
python manage.py loaddata option/fixtures/option.json || echo "⚠️ Fixtures Option déjà chargées ou introuvables."

echo "✅ Démarrage du serveur Django..."
exec python manage.py runserver 0.0.0.0:8080
