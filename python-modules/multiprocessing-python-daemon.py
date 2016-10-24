# coding:utf-8

from daemon import DaemonContext
from multiprocessing import Process
import sys
import traceback

def output(msg):
    with open('/home/oraant/study/python-modules/tmp.log', 'a') as file:
        file.write(str(msg) + '\n')

def flush(msg):
    with open('/home/oraant/study/python-modules/tmp.log', 'w') as file:
        file.write((msg) + '\n')

flush('---')

p1 = Process(target=output, args=('this is child1',))

context = DaemonContext()
context.detach_process=False

with DaemonContext():
    
    output(p1)
    
    output('in daemon.')

    p2 = Process(target=output, args=('this is child2',))
    p2.start()
    output('p2 started')

    try:
        p1.start()
    except Exception, e:
        output(Exception)
        output(repr(e))
    output('p1 started or failed.')

    output('this is father')


# 默认的，在Daemon化的时候，会关闭文件描述符，更换工作路径，从进程组分离等，所以会导致在外面建立的进程无法正常启动，并抛出如下异常：
# AssertionError('can only start a process object created by current process',)

# 注意，在output中，应该使用绝对路径，否则换成守护进程后，就会更换路径
# 注意，在output中，应该使用str()将所要展示的东西包起来，否则这里容易发生类型错误但守护进程不抛出异常。所以不好排错。
