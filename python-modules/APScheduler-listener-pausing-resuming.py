# coding:utf:8


#from apscheduler.schedulers.blocking import BlockingScheduler as Scheduler
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from apscheduler.events import EVENT_JOB_ERROR
import time
import logging

logging.basicConfig()

num = 1

def myfunc1():
    print 'hello, this is 1.'

def myfunc2():
    global num
    if num == 1:
        print 'hello, this is 2.'
    else:
        raise StandardError('num is not 1')

def myfunc3():
    global num
    if num == 1:
        print 'hello, this is 3.'
    else:
        raise StandardError('num is not 1')

def change():
    global num
    if num == 1: num = 2;

def listener(event):
    try:
        print event
        raise event.exception
    except Exception as e:
        print '---', e, '---'
        jobs = scheduler.get_jobs()
        for job in jobs:
            scheduler.pause_job(job.id)
        print 'haha'
        #scheduler.shutdown()
        #scheduler.remove_all_jobs()
        #global num
        #num = 1
        #scheduler.shutdown()

scheduler = Scheduler()
scheduler.add_job(myfunc1, 'interval', seconds=3)
scheduler.add_job(myfunc2, 'interval', seconds=3)
scheduler.add_job(myfunc3, 'interval', seconds=3)
scheduler.add_job(change,  'interval', seconds=4)
scheduler.add_listener(listener, EVENT_JOB_ERROR)
scheduler.start()

time.sleep(2)
print scheduler.running
time.sleep(5)
print scheduler.running

# 结论：
# 如果在监听中，把scheduler暂停，则监听自己也停了。
# 如果在监听中，把scheduler关闭，则监听自己也会停。
# pause_job可以只暂停制定job，而不暂停listener。
# 两个线程同时报错时，应该怎样关闭schedulers？
# log = logging.getLogger('apscheduler.executors.default')，即便在listener中处理了异常，APS还是照样会尝试记录日志
# 暂停线程时，是否可以把监听之外的线程除掉不暂停
# 在监听中，可以修改全局变量
