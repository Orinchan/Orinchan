#!/bin/bash
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate --verbosity 3

echo "Loading initial data..."
if [ -f "backup.json" ]; then
    python manage.py loaddata backup.json
else
    echo "No backup.json found, skipping data load."
fi

echo "Build completed successfully!"