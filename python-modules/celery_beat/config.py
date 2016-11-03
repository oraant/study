from datetime import timedelta
from time import time

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_IMPORTS = ['tasks']

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },

    'output-every-3-seconds': {
        'task': 'tasks.output',
        'schedule': timedelta(seconds=3),
        'args': ('%s - hello3~\n' % time(),)
    },

    'output-every-2-seconds': {
        'task': 'tasks.output',
        'schedule': timedelta(seconds=2),
        'args': ('%s - hello2~\n' % time(),)
    },
}

CELERY_TIMEZONE = 'UTC'
