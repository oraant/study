# coding:utf:8

# 测试调度器的暂停效果，用后台调度的方式就相当于多线程了吧

#from apscheduler.schedulers.blocking import BlockingScheduler as Scheduler
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from apscheduler.events import EVENT_JOB_ERROR
import time

def myfunc1():
    print 'hello, this is 1.'

def myfunc2():
    print 'hello, this is 2.'

def myfunc3():
    print 'hello, this is 3.'

def listener(event):
    try:
        raise event.exception
    except Exception as e:
        print e

scheduler = Scheduler()
scheduler.add_job(myfunc1, 'interval', seconds=0.4)
scheduler.add_job(myfunc2, 'interval', seconds=0.3)
scheduler.add_job(myfunc3, 'interval', seconds=0.2)

scheduler.start()


print '------- waiting for 3 seconds.'
time.sleep(3)

print '------- pauseing for 3 seconds.'
scheduler.pause()
time.sleep(3)

print '------- resumeing and wait 3 seconds'
scheduler.resume()
time.sleep(3)

print '------- resumeing and wait 3 seconds'
print 'all done'
