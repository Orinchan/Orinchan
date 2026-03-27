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

python manage.py makemigrations

echo "5) Running migrations"
python manage.py migrate --no-input

echo "6) Create Django superuser if not exists (uses env vars)"
# Variables esperadas (configura en Render Dashboard):
# DJANGO_SUPERUSER_USERNAME
# DJANGO_SUPERUSER_EMAIL
# DJANGO_SUPERUSER_PASSWORD
python - <<'PY'
import os
from django.contrib.auth import get_user_model
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if not username or not password:
    print("  - DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD not set; skipping superuser creation")
else:
    User = get_user_model()
    if User.objects.filter(username=username).exists():
        print(f"  - Superuser '{username}' already exists; skipping creation")
    else:
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"  - Superuser '{username}' created")
PY

echo "=== Build completed successfully ==="
