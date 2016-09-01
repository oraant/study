# coding:utf-8

from os import getpid
from time import sleep
from multiprocessing import Process, Pipe
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler


class MyJob():

    def __init__(self, name):
        """
        Init things.
        :param name: str: name
        """
        self.name = name
        self.scheduler = Scheduler()
        self.keep = True  # class attribute or instance attribute
        self.father, self.child = Pipe()

    def _flush(self):  # flush file
        with open("/home/oraant/study/data/test.log", "w") as file:
            file.write('-----------\n')

    def _log(self, msg):
        with open("/home/oraant/study/data/test.log", "a") as file:
            file.write(msg+"\n")

    def print_keep(self):
        self._log("self keep is " + str(self.keep) + ". keep id is " + str(id(self.keep)))

    def _run(self):
        log_msg = "child %s is running... pid is %d" % (self.name, getpid())
        self.scheduler.add_job(self._log, 'interval', seconds=0.5, args=(log_msg,))
        self.scheduler.start()
        self._listen()

    def _listen(self):
        while True:
            msg = self.child.recv()
            if msg == 'stop':
                self.scheduler.shutdown()
                self.child.send("%s done" % self.name)
                break
            elif msg == 'status':
                self.child.send("%s is running" % self.name)


    def start(self):
        self._flush()
        p = Process(target=self._run)
        p.start()

    def stop(self):
        self.father.send("stop")
        print self.father.recv()

    def status(self):
        self.father.send("status")
        print self.father.recv()


# start job with a queue
job1 = MyJob('job1')
job2 = MyJob('job2')
job1.start()
job2.start()
print 'started'


# wait and stop it
print 'wait 3s and check status.'
sleep(3)
job1.status()
job2.status()


# wait 3s.
print 'wait 3s and stop.'
sleep(3)
job1.stop()
job2.stop()

print 'all done'

# 结论：通过队列实现进程间通信，在接受端收到队列传递过来的信息后，可以关闭后台执行的scheduler。
# 队列可以多个进程间一起用，但是一个内容被取出去后，别人就取不到了。谁先取谁后取，是随机的。
# 一个类可以同时包含开启方法和关闭方法，然后针对一个队列进行操作。父进程中通过stop给队列发消息，子进程中接受到队列的消息则stop等。
