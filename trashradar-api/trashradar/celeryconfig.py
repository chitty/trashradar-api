from django.conf import settings

BROKER_URL = settings.BROKER_URL
CELERY_RESULT_BACKEND = BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'PST8PDT'
CELERYBEAT_SCHEDULE = {}
CELERYBEAT_SCHEDULE = {}
