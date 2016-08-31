# coding:utf-8

import daemon, signal, time

def log(msg):
    with open('/var/log/tttt.log', 'a') as file:
        file.write(msg + "\n")

def main_job():
    while True:
        time.sleep(1)
        log("hello")

def main_reload():
    log("reload")

def main_stop():
    log("stop")

context = daemon.DaemonContext()
context.signal_map = {
    signal.SIGTERM: main_stop,
    signal.SIGHUP: main_stop,
    signal.SIGUSR1: main_reload,
}

with context:
    main_job()
