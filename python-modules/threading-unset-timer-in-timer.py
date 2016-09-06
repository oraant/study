# coding:utf-8

import threading as T
from time import sleep

def f():
    global t
    print '------------- in f()'
    print T.enumerate()
    print 't =', t
    t=None
    print 't =', t
    print 'done'
    print T.enumerate()

t = T.Timer(1, f)
t.start()



sleep(3)

print '-----------all'
print T.enumerate()


# 结论：
# t引用线程，在线程中将t设置为None，即取消t对线程的引用，对线程没有影响
