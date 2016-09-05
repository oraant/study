# coding:utf-8

import threading as T
from time import sleep

def f():
    print 'hello'

t = T.Timer(3, f)

print '---------name'
print t.name
t.name = 'myname'
print t.name

print '---------ident'
print t.get_ident()
t.ident = 111222333444555
print t.ident


t.start()

sleep(1)

print '-----------all'
print T.enumerate()
