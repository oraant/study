# coding:utf-8

from cloghandler import ConcurrentRotatingFileHandler as CRFHandler
from logging import getLogger, INFO
import os
from time import ctime, sleep
from random import random
from multiprocessing import Process as P

logfile = os.path.abspath("/home/oraant/study/data2/test2.log")
loghandler = CRFHandler(logfile, 'a', 1024*4, 3)

logger = getLogger()
logger.addHandler(loghandler)
logger.setLevel(INFO)


def log(name):

    pid = os.getpid()
    msg = str(pid) + ', ' + name

    for i in range(40):
        time = random()/10
        sleep(time)
        logger.info(msg)

p1 = P(target=log, args=('p1',))
p2 = P(target=log, args=('p2',))
p3 = P(target=log, args=('p3',))

p1.start()
p2.start()
p3.start()
log('main')

# 结论：多进程不冲突，而且可以循环写
