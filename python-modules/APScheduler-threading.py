# coding:utf-8
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.events import EVENT_JOB_ERROR
import threading as T
from time import sleep
import logging
logging.basicConfig()

executors = {
    'default': ThreadPoolExecutor(3)
}
s = Scheduler(executors=executors)


def show(t, msg):

    print '-------', T.active_count(), '|', msg

    all_threads = T.enumerate()
    for thread in all_threads:
        if thread is t:
            print thread, '*'
        else:
            print thread

    print 

v = 0
def f():
    T.current_thread().name = 'job'
    show(T.current_thread(), 'the job. count is '+str(v))
    global v
    if v == 4:
        v = v+1
        raise KeyError('a')
    v = v+1


def listener(event):
    return
    T.current_thread().name = 'listener'
    show(T.current_thread(),'the listener.')
    sleep(1)
    s.shutdown()
    show(T.current_thread(),'the listener.')
        

s.add_job(f, 'interval', seconds=1)
s.add_listener(listener, EVENT_JOB_ERROR)
s.start()

sleep(4)
s.shutdown()
show('','main')

sleep(10000)

# 结论：
# APScheduler（以下简称AP）有两种方式的进程调度，一种是线程池方式的，一种是进程池方式的。默认是线程池式的，且最大线程数为10。
# 每次到了调度时间时，AP首先会在线程池中添加一个新的线程，除非线程池已经满了。
# 然后，从线程池中随意调取一个线程，用来执行要执行的任务。
# 
# 抛出异常，同样会使用线程池中的线程去调用监听异常的回调函数。
