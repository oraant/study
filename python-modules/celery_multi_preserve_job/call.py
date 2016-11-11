# coding:utf-8

from tasks import raiseerror, preserve, handle_signal
from time import sleep
from sys import stdout
from threading import Thread

def check():
    for i in range(1100):
        sleep(0.01)
        stdout.flush()
        msg = '\r' + r.state + ' ' + r.status
        stdout.write(msg)
        stdout.flush()
    print

r = handle_signal.delay(10)
Thread(target=check).start()
sleep(4)
r.revoke(terminate=True, signal='SIGKILL')
#r2 = handle_signal.delay(10)

# 结论
# 只有revoke时，好像没啥效果，后面紧跟着调用其delay时，仍然会成功执行
# 加了terminate时，程序就会报错，但是可以自己接收sigterm信号并处理。如果不舍值，即使处理了，state也会变成revoke
# 加了signal后，可以发送个别的signal，然后自己在tasks里去接收并处理，但是signal不能是SIGKILL
