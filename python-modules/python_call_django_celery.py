# coding:utf-8

# # tree /home/oraant/test/django_celery/|grep -v .pyc
# /home/oraant/test/django_celery/
# ├── db.sqlite3
# ├── django_celery
# │   ├── celery.py     # ----------
# │   ├── __init__.py
# │   ├── settings.py
# │   ├── urls.py
# │   ├── wsgi.py
# ├── manage.py
# └── myapp
#     ├── admin.py
#     ├── apps.py
#     ├── __init__.py
#     ├── migrations
#     │   ├── 0001_initial.py
#     │   ├── __init__.py
#     ├── models.py
#     ├── tasks.py      # ---------
#     ├── tests.py
#     ├── views.py
# 
# 3 directories, 28 files


import os, sys
sys.path.append('/home/oraant/test/django_celery/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

import django
django.setup()

from myapp.tasks import add
print add.delay(1, 2).get()
