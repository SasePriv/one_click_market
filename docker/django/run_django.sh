#! /bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --noinput -c -v 0

# Set auto-reload on source code changes only for LOCAL
if [ "${DEPLOY_ENVIRONMENT:-x}" = "LOCAL" ]; then
    CONF_GUNICORN_EXTRA_ARGS="$CONF_GUNICORN_EXTRA_ARGS --reload"
    echo "Enabling autoreload"
fi

gunicorn django_project_config.wsgi:application --bind 0.0.0.0:8000