# Запуск приложения #

- docker-compose up -d
- docker-compose run django python manage.py migrate
- docker-compose run django python manage.py createsuperuser

- celery -A netology_pd_diplom.celery worker --loglevel=info
