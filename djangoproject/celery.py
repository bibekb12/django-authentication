# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.settings")
# app = Celery("djangoproject", broker="redis://localhost:6379/0")
# app.config_from_object("django.conf:settings", namespace="CELERY")
# app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request!r}.format(self.request)")


# @app.task(bind=True)
# def view_queue(self):
#     i = app.control.inspect()
#     active_tasks = i.active()
#     scheduled_tasks = i.scheduled()
#     reserved_tasks = i.reserved()
#     print(f"Active tasks: {active_tasks}")
#     print(f"Scheduled tasks: {scheduled_tasks}")
#     print(f"Reserved tasks: {reserved_tasks}")

from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings  # This line is need debugging
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.settings")

app = Celery("djangoproject")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.broker_connection_retry_on_startup = True

app.conf.broker_connection_max_retries = 5

logger = app.log.get_default_logger()
