# Запуск приложения #

- docker-compose up -d
- docker-compose run django python manage.py createsuperuser


# Запуск Celery если приложение запущено без докера #
- celery -A netology_pd_diplom.celery worker --loglevel=info
