# coding:utf-8

from os import getpid
from time import sleep
from multiprocessing import Process, Queue
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler


class MyJob():

    def __init__(self, name, queue):
        """
        Init things.
        :param name: str: name
        :param queue: multiprocessing.Queue
        """
        self.name = name
        self.scheduler = Scheduler()
        self.keep = True  # class attribute or instance attribute
        self.queue = queue

    def _flush(self):  # flush file
        with open("/home/oraant/study/data/test.log", "w") as file:
            file.write('-----------\n')

    def _log(self, msg):
        with open("/home/oraant/study/data/test.log", "a") as file:
            file.write(msg+"\n")

    def print_keep(self):
        self._log("self keep is " + str(self.keep) + ". keep id is " + str(id(self.keep)))

    def _run(self):
        self._log("hello %s, pid is %d" % (self.name, getpid()))

    def start(self):
        self._flush()
        self.scheduler.add_job(self._run, 'interval', seconds=0.5)
        self.scheduler.start()

        while True:
            if self.queue.get(True):
                self.scheduler.shutdown()
                break

    def stop(self):
        self.queue.put(True)

# start job with a queue
queue = Queue()
job1 = MyJob('job1', queue)
job2 = MyJob('job2', queue)
p1 = Process(target=job1.start)
p2 = Process(target=job2.start)
p1.start()
p2.start()
print 'started'


# wait and stop it
print 'wait 3s and stop it.'
sleep(3)
job1.stop()
sleep(1)
job2.stop()
print 'stop'


# wait 3s.
print 'wait 3s and exit.'
sleep(3)

# 结论：通过队列实现进程间通信，在接受端收到队列传递过来的信息后，可以关闭后台执行的scheduler。
# 队列可以多个进程间一起用，但是一个内容被取出去后，别人就取不到了。谁先取谁后取，是随机的。
# 一个类可以同时包含开启方法和关闭方法，然后针对一个队列进行操作。父进程中通过stop给队列发消息，子进程中接受到队列的消息则stop等。
