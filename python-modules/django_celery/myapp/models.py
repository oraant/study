from __future__ import unicode_literals

from django.db import models
from .tasks import mainjob
from celery.result import AsyncResult

# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    task = models.CharField(max_length=100, blank=True, null=True)

    def start(self):
        if self.task and AsyncResult(self.task).state == 'RUNNING':
            return 'you need to stop the task of %s' % self.name

        self.task = mainjob.delay(self.name)
        self.save()
        return 'start successfully for %s' % self.name

    def stop(self):
        if not self.task:
            return 'you need to start the task of %s' % self.name
        AsyncResult(self.task).revoke(terminate=True, signal='SIGUSR1')
        #, wait=True, timeout=3)
        return 'stop successfully for %s' % self.name

    def clear(self):
        self.task = None
        self.save()
        return 'clear successfully for %s' % self.name

    def status(self):
        if not self.task:
            return 'Nothing'
        return AsyncResult(self.task).state
