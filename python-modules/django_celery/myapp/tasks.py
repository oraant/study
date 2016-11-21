from __future__ import absolute_import
from celery import shared_task
from threading import Event, Thread
from signal import signal, alarm, pause, SIGTERM, SIGUSR1, SIGALRM
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
#from apscheduler.schedulers.blocking import BlockingScheduler as Scheduler
from apscheduler.events import EVENT_JOB_ERROR
from time import time, sleep
import logging


@shared_task
def add(x, y):
    return x + y

@shared_task(bind=True)
def see(self):
    out_output(type(self), '/tmp/aaaaaaaaaaaaa.log')
    out_output(str(self), '/tmp/aaaaaaaaaaaaa.log')
    out_output(dir(self), '/tmp/aaaaaaaaaaaaa.log')
    out_output(self.__class__, '/tmp/aaaaaaaaaaaaa.log')
    out_output(self.__name__, '/tmp/aaaaaaaaaaaaa.log')
    out_output(self.__doc__, '/tmp/aaaaaaaaaaaaa.log')
    #out_output(self.__class__, '/tmp/aaaaaaaaaaaaa.log')

@shared_task(bind=True)
def mainjob(self, name):

    self.filename = '/tmp/dc/django_celery_%s.log' % name

    # prepare
    out_output(str(self.request.retries), self.filename)
    self.default_retry_delay = 5
    self.max_retries = 2
    self.count = 0

    # reply_to = self.request.reply_to
    # out_output(reply_to, self.filename)
    # out_output(dir(reply_to), self.filename)
    # out_output(reply_to.__doc__, self.filename)
    # out_output(type(reply_to), self.filename)

    jlogger = logging.getLogger('apscheduler.scheduler')
    jlogger.setLevel(logging.ERROR)
    scheduler = Scheduler(logger=jlogger)
    self.update_state(state='RUNNING')

    # shutdown 
    def shutdown(a, b):
        output('shuting')
        scheduler.shutdown()
        output('down - %s' % time())

    def terminate(a, b):
        output('terminating')
        scheduler.shutdown()
        output('down - %s' % time())

    def retryer(a, b):
        out_output('before retry', self.filename)
        scheduler.shutdown()
        raise self.retry()
        out_output('after retry', self.filename)


    signal(SIGUSR1, shutdown)
    signal(SIGTERM, terminate)
    signal(SIGALRM, retryer)

    # listen
    def listener(event):
        try:
            raise event.exception
        except Exception as e:
            out_output(e, self.filename)
            [job.pause() for job in scheduler.get_jobs()]
            alarm(1)

    scheduler.add_listener(listener, EVENT_JOB_ERROR)

    # add job and start
    def output(msg):
        self.count += 1
        #if self.count == 9: raise StandardError('haha')
        with open(self.filename, 'a') as file:
            file.write('(%s - %s) %s\n' % (time(), name, msg))

    scheduler.add_job(output, 'interval', args=('--a',), seconds=1)
    sleep(0.5)
    scheduler.add_job(output, 'interval', args=('------b',), seconds=1)
    #scheduler.add_job(output, 'interval', args=('--b',), seconds=3)
    scheduler.start()

    # wait for retry
    pause()

i = 0
def out_output(msg, filename):
    global i
    i += 1
    #if i == 8: raise StandardError('haha')
    #if i == 5: raise StandardError('haha')
    with open(filename, 'a') as file:
        file.write('[%s] %s\n' % (time(), msg))

@shared_task(bind=True)
def testretry(self):
    # prepare
    out_output(str(self.request.retries),'/tmp/dc/django_celery_testretry.log')
    self.default_retry_delay = 2
    self.max_retries = 2

    output('--start--')
    sleep(1)

    self.retry()
