pre-release: python manage.py makemigrations
release: python manage.py migrate && python manage.py collectstatic --dry-run --noinput

web: gunicorn website.wsgi