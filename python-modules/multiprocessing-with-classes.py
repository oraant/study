# coding:utf-8
from time import sleep
from multiprocessing import Process

class C():

    keep = True

    def flush(self):  # flush file
        with open("/home/oraant/study/data/test.log", "w") as file:
            file.write('-----------\n')

    def log(self, msg):
        with open("/home/oraant/study/data/test.log", "a") as file:
            file.write(msg+"\n")

    def run(self):
        self.flush()
        while self.keep:
            sleep(1)
            self.log("running " + str(id(self)))
            self.print_keep()

    def print_keep(self):
        self.log("self keep is " + str(self.keep) + ". keep id is " + str(id(self.keep)))

    def stop(self):
        self.keep = False
        self.log("stoping")
        self.print_keep()
        self.log("")

c = C(); print id(c)

p = Process(target=c.run)
p.start()
sleep(3); print 'started, wait for 3s.'

c.stop(); print 'stoped, then wait 3s.'
sleep(3); print 'all done'

# 子进程复制了父进程中的c对象，尽管两个对象的id是相同的，但是两个对象中的keep值是不同的
