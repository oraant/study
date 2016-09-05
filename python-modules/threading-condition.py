import threading as T
import time


def waiter():
    with condition:
        print 'waiting'
        condition.wait()
        print 'done'

def notice():
    with condition:
        condition.notifyAll()
        print 'notify all'

condition = T.Condition()

t1 = T.Thread(target=waiter).start()
t2 = T.Thread(target=waiter).start()
print 'started'

time.sleep(3)
T.Thread(target=notice).start()
print 'send done'
