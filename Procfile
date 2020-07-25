pre-release: python manage.py makemigrations
release: python manage.py migrate && python manage.py collectstatic

web: gunicorn website.wsgi