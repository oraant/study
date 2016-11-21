from threading import Lock, Thread
from time import sleep

mutex = Lock()

def f(msg):
    with mutex:
        for i in range(5):
            print '---%s---' % msg
            sleep(0.1)
        raise StandardError('haha')

def m(msg):
    for i in range(5):
        print '---%s---' % msg
        sleep(0.1)
    raise StandardError('haha')

t1 = Thread(target=f, args=('a',))
t2 = Thread(target=f, args=('b',))

#t1 = Thread(target=m, args=('a',))
#t2 = Thread(target=m, args=('b',))

t1.start()
t2.start()

t1.join()
t2.join()
