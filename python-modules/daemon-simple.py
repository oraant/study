# coding:utf-8

import random
from daemon import DaemonContext
from time import sleep

def output(msg):
    with open('/var/log/oet/test.log', 'a')as file:
        file.write(msg)

def flush(msg):
    with open('/var/log/oet/test.log', 'w')as file:
        file.write(msg)

def pre_main():
    flush('hahahaha')

def main_job():
    while True:
        output(str(random.random()))
        sleep(1)

with DaemonContext():
    pre_main()
    main_job()
