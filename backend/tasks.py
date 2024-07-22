from django.core.mail import EmailMultiAlternatives
from netology_pd_diplom.celery import app
from celery import shared_task
from django.conf import settings



@shared_task
def send_mail(title, body, from_adress, to_adress):
    msg = EmailMultiAlternatives(
        title,
        body,
        from_adress,
        to_adress,
    )
    msg.send()
    return True




