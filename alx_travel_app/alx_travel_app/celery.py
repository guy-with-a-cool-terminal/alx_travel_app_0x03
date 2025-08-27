import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

# create celery app
app = Celery('alx_travel_app')

# load configuration from settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# automatically discover tasks
app.autodiscover_tasks()

# debug
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')