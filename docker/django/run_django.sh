#! /bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --noinput -c -v 0

gunicorn django_project_config.wsgi:application --bind 0.0.0.0:8000