import cx_Oracle
from threading import Timer
from time import sleep

def close():
    print 'before db.cancel()'
    #db.cancel()
    c.close()
    print 'after db.cancel()'

def run():
    print 'running'
    c.execute("select open_mode from v$database")
    print 'executed'
    data = c.fetchall()
    print data

def sl():
    print 'befor wait 1s'
    sleep(1)
    print 'wait done'

db = cx_Oracle.connect("system", "oracle", "192.168.10.107:1521/db11g")
print 'connected, 2s to close the network'
sleep(2)

c = db.cursor()
print 'cursored, 2s to close the network'
sleep(2)

t = Timer(2, close)
t.start(); print 'start threading for 2s'
run()
t.cancel()
