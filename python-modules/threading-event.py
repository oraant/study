import threading as T
from time import sleep

closed = T.Event()

def f():
    sleep(5)
    closed.set()
    print 'end.'

t = T.Thread(target=f)
t.start()

while True:
    if closed.wait(2):
        closed.clear()
        print 'ended'
        break

    print 'running'
