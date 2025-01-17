from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.forms import Widget
from django.contrib.auth.models import User


@shared_task
def send_registration_email_notification(username, email, password):
    subject = "Registration successful"
    message = f"Hi {username}, thank you for registering in our site. Your password is {password}"
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email])


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y, z):
    return x * y * z


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.object.get(id=widget_id)
    w.name = name
    w.save()


@shared_task
def send_mail(user_pk):
    user = User.object.get(pk=user_pk)
    send_mail.delay_on_commit(user.pk)
