from time import time
from time import sleep

def f(seconds):
    print 'start wait'
    sleep(seconds)
    print 'end wait'

l = [1]*5

def gap(x):
    old_time = time()
    x()
    gap_time = time()-old_time
    print gap_time
    return gap_time

def f1():
    for i in l:
        f(i)

def f2():
    map(lambda x:f(x), l)

print '---'
gap(f1)
print '---'
gap(f2)
print '---'
