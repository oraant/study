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

import sys
sys.path.append('/home/oraant/test/django_celery/')

from myapp.views import test_add
print test_add(1, 2)
