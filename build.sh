#!/bin/bash
set -o errexit

echo "Installing dependencies..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "Collecting static files..."
python3 manage.py collectstatic --no-input

echo "Build completed successfully!"
