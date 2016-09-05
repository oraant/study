from threading import Timer
from time import sleep

def sayhello():
    print "hello"
    sleep(1)
    print "world"

t = Timer(1, sayhello)
t.start()

t = Timer(1, sayhello)
t.start()

sleep(1.5)
t.cancel()
t.cancel()
t.cancel()
t.cancel()
print 'canceled'

# 结论：
# 即使线程执行完了，也可以调用其cancel函数，且不会有异常
