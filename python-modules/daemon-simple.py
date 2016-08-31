# coding:utf-8

import daemon, random

def main_job():
    while True:
        print random.random()

with daemon.DaemonContext():
    main_job()
