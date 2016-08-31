# coding:utf-8
from time import sleep
import os
from multiprocessing import Process

# handle files


def flush():  # flush file
    with open("/home/oraant/study/data/test.log", "w") as file:
        file.write('-----------\n')


def log(msg):  # write msg to file
    with open("/home/oraant/study/data/test.log", "a") as file:
        file.write(msg+"\n")


def run():  # keep write data
    flush()
    while True:
        sleep(1)
        log('hello')

# logic method


def behind(time=2):  # some other code
    print 'behind code running'
    sleep(time)
    print 'behind code end'


def output_pid(p):  # output father and child's pid
    print 'father is', os.getpid()
    print 'child is', p.pid
    print 'command is:\n pstree -ap %s' % os.getpid()

# make child process


def f1():  # process will blocking main from exiting. but statements behind will keep running.
    p = Process(target=run)
    p.start()
    output_pid(p)
    behind()


def f2():  # with join, join() method will blocking code.behind() will never run until children done.
    p = Process(target=run)
    p.start()
    p.join()
    behind()


def f3():  # with join and join timeout parameter, method will blocking code for timeout seconds, children will not end.
    p = Process(target=run)
    p.start()
    p.join(10)
    output_pid(p)
    behind()


def f4():  # with daemon, if main quit, process will exit too.
    p = Process(target=run)
    p.daemon = True
    p.start()
    output_pid(p)
    behind(10)


def f5():  # with daemon and join, process will blocking code.
    p = Process(target=run)
    p.daemon = True
    p.start()
    p.join()
    behind(10)


def f6():  # with join and daemon timeout, process will blocking code for timeout seconds or children end.
    p = Process(target=run)
    p.daemon = True
    p.start()
    p.join(3)
    behind(10)

f6()

# 结论：
# process的daemon只决定主程序退出时，进程是否退出。
# process的join()只决定什么时候执行后面的程序。
