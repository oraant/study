from datetime import timedelta
from time import time

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_IMPORTS = ['tasks']
CELERY_TIMEZONE = 'UTC'
