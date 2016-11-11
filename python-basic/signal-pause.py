# coding:utf-8
import signal
import os

def handler(a,b):
    print 'handling'
signal.signal(signal.SIGTERM, handler)

print os.getpid()
signal.pause()
print 'after pause'

# 结论：
# signal.pause只是暂停，一旦接收到信号，就会往下执行
