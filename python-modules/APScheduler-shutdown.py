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
    sleep(4)
    global v
    if v == 4:
        v = v+1
        raise KeyError('a')
    v = v+1

def close():
    show('','closing, shutting ...')
    s.shutdown()
    show('','closing, done')


show('','main')

s.add_job(f, 'interval', seconds=5)
s.start()

sleep(11)
T.Thread(target=close).start()
sleep(1)
show('','main, shutting ...')
s.shutdown(wait=False)
show('','main, done')

sleep(10000)

# 结论：
# 关闭时，如果shutdown时如果正好有正在执行的任务，那么shutdown会阻塞等待其完成。否则，shutdown立马就执行了。
# 关闭时，如果scheduler没有在运行，就会报错：   apscheduler.schedulers.SchedulerNotRunningError: Scheduler is not running
# 关闭时，如果在一个线程中调用了shutdown但是hang住了，这时想再开个线程调用shutdown(wait=False)，这是不行的，还是会报上面的错误
