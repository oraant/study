# coding:utf-8
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from time import sleep

s = Scheduler()

def output():
    for i in 'hello':
        sleep(0.4)
        print i


s.add_job(output, 'interval', seconds=3)
s.start()
print 'started'

sleep(10)


print 'trying to shutdown'
#s.shutdown(wait=False)
#s.shutdown(wait=True)
s.shutdown()
print 'shutdown complete'

#sleep(5)

# 结论：
# shutdown时，无论是否wait，都不会强中断job线程。
# 假设shutdown时，有正在执行的任务，那么：
# wait为True，则shutdown等job全执行完再执行后面的。好比饭店要关门了，店长说：“要关门啦！大家吃完后就得走啦，我等你们吃完再关门，然后去接孩子。”
# wait为False，则shutdown告诉job线程“一会自己关上，我先去干别的”，好比“大家吃完就走哈，我不等你们了，我得先去接孩子！”
# wait默认为True
