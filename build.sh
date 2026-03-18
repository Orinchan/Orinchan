#!/bin/bash
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate --verbosity 3

python manage.py dumpdata > backup.json

echo "Build completed successfully!"
