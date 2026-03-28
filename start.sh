#!/bin/bash
set -o errexit

echo "Applying migrations..."
python3 manage.py migrate --noinput

echo "Starting Gunicorn..."
exec gunicorn -c gunicorn_config.py django_porfolio.wsgi:application
