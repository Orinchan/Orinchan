#!/bin/bash
set -o errexit
set -o pipefail
set -u

echo "=== Build start ==="

echo "1) Ensure pip is up to date"
python -m pip install --upgrade pip

echo "2) Installing dependencies from requirements.txt"
python -m pip install -r requirements.txt

echo "3) Ensure static directory exists"
PROJECT_DIR="$(pwd)"
STATIC_DIR="${PROJECT_DIR}/static"
if [ ! -d "$STATIC_DIR" ]; then
  echo "  - Creating static directory at $STATIC_DIR"
  mkdir -p "$STATIC_DIR"
fi

echo "4) Collecting static files"
python manage.py collectstatic --no-input

echo "5) Running migrations"
python manage.py migrate --no-input

echo "=== Build completed successfully ==="
