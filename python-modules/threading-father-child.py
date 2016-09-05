# coding:utf-8

import threading as T
from time import sleep

def show(msg='showing'):
    print '--------------------', msg
    for t in T.enumerate():
        print t

def father():
    show("in father")
    c = T.Thread(target=child, name="child")
    #c.setDaemon(True)
    c.start()
    show("end father")

def child():
    while True:
        sleep(1)
        show('child')

f = T.Thread(target=father, name="father")
#f.setDaemon(True)
f.start()


# while True:
#     sleep(1)
#     show('main')

# 结论：
# 创建新线程的线程死掉，也不影响生成的线程。即便setDaemon(True)也一样
# setDaemon为False(默认)时，主线程结束后依然存在，但是状态是stopped。
# setDaemon为True时，主线程结束后，daemon也跟着结束了。（当只剩下daemon线程时，整个的python程序就会退出）
