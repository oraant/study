# coding:utf-8
from multiprocessing import Process, Pipe
from time import sleep

left, right = Pipe()


# self save and get.first in first out.
print '--------------'
left.send("hello1")
left.send("hello2")
print right.recv()
print right.recv()

# two ends can send msg at the same time.
print '--------------'
left.send("hello c")
right.send("hello f")
print right.recv()
print left.recv()


# system just copy ends of the pipe when fork, doesn't copy pipe.
"""
print '--------------'
def children():
    left.send("children send into parent ends")

def main():
    left.send("father send into parent ends")
    Process(target=children).start()
    left.send("father send into parent ends")

    print right.recv()
    print right.recv()
    print right.recv()

main()
"""

# what will happen if recv before send.
print '--------------'

def children():
    print right.recv()

def main():
    Process(target=children).start()
    sleep(1)
    left.send("hello,hey ya")

main()

# 结论：
# 管道可以自存自取，遵循先进先出
# 双通道的管道，两端可以同时发送信息而不冲突
# Pipe()函数返回管道的两端。fork时，不复制管道，只复制管道的两端。
# 父进程和子进程都有管道的两端，假设同时从一端读，或从一端写，管道可能会被毁坏。这个脚本只是为了实验，所以这么做了。
