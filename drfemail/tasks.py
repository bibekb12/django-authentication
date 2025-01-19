from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail as django_send_mail


@shared_task
def send_registration_email_notification(username, email, password):
    subject = "Registration successful"
    message = f"Hi {username}, Thank you for registering in our site.Your password is: {password}"
    email_from = settings.EMAIL_HOST_USER
    django_send_mail(subject, message, email_from, [email])


@shared_task
def send_delete_email_notification(username, email):
    subject = "Deletion successful"
    message = f"Hi {username}, Your account has been deleted successfully."
    print("username --", email)
    email_from = settings.EMAIL_HOST_USER
    django_send_mail(subject, message, email_from, [email])
