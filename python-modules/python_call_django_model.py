# coding:utf-8

# # tree /home/oraant/test/django_celery/|grep -v .pyc
# /home/oraant/test/django_celery/
# ├── django_celery
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
#     │   ├── __init__.py
#     ├── models.py
#     ├── tests.py
#     └── views.py
# 
# 3 directories, 25 files

import os, sys
sys.path.append('/home/oraant/test/django_celery/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

import django
django.setup()

from myapp.models import TestModel
print TestModel.objects.all()
