import threading as T
#from apscheduler.schedulers.blocking import BlockingScheduler as Scheduler
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from time import sleep

executors = {'default': ThreadPoolExecutor(3)}
s = Scheduler(executors=executors)

def show(msg='a'):
    print '--------------------', msg
    for t in T.enumerate():
        print t

def output():
    print '.'

def close(time = 5):
    sleep(time)
    show("closing")
    s.shutdown()
    show("closed")

s.add_job(output, 'interval', seconds=1)
s.start()
t = T.Thread(target=close, name="close")
t.start()

#for i in range(6):
while True:
    sleep(1)
    show('main')

# 结论：
# 可以新开一个线程，调用scheduler的shutdown函数，其内部会设置event的相关状态，关闭进程
