from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netology_pd_diplom.settings')
app = Celery("diplom",
             broker_connection_retry_on_startup = True)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


