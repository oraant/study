# coding:utf-8

import threading as T
import logging

from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler


logging.basicConfig()
s = Scheduler()
mutex = T.Lock()


def show(name, l):
    if mutex.acquire(1):
        for i in l:
            print i, 
        sleep(2)
        print 'name is', name
        mutex.release()

def f1(): show(1, ['1']*7)
def f2(): show(2, ['2']*7)
def f3(): show(3, ['3']*7)
def f4(): show(4, ['4']*7)
def f5(): show(5, ['5']*7)
def f6(): show(6, ['6']*7)
def f7(): show(7, ['7']*7)
def f8(): show(8, ['8']*7)
def f9(): show(9, ['9']*7)

T.Thread(target=f1).start()
T.Thread(target=f2).start()
T.Thread(target=f3).start()
T.Thread(target=f4).start()
T.Thread(target=f5).start()
T.Thread(target=f6).start()
T.Thread(target=f7).start()
T.Thread(target=f8).start()
T.Thread(target=f9).start()

sleep(100)
