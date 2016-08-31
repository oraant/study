# coding:utf-8

from time import sleep
from multiprocessing import Process
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler

class MyJob():


    def __init__(self, queue):
        scheduler = Scheduler()
        keep = True  # class attribute or instance attribute
        self.queue = queue

    def flush(self):  # flush file
        with open("/home/oraant/study/data/test.log", "w") as file:
            file.write('-----------\n')

    def log(self, msg):
        with open("/home/oraant/study/data/test.log", "a") as file:
            file.write(msg+"\n")

    def print_keep(self):
        self.log("self keep is " + str(self.keep) + ". keep id is " + str(id(self.keep)))

    def run(self):
        self.log("hello")

    def start(self):
        self.flush()
        self.scheduler.add_job(self.run())

    def waiting_to_stop(self):
        while True:
            if self.queue.get()


c = C(); print id(c)

p = Process(target=c.run)
p.start()
sleep(3); print 'started, wait for 3s.'

c.stop(); print 'stoped, then wait 3s.'
sleep(3); print 'all done'

# 子进程复制了父进程中的c对象，尽管两个对象的id是相同的，但是两个对象中的keep值是不同的