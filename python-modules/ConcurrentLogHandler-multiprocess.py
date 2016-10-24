# this script may hang when number is 60, try it again and again, you will find it hang for 5 seconds, and log file is broken.
# command is    cat tmp.log |sort -Vu |wc -l

from multiprocessing import Process as P
import logging
#from logging.handlers import RotatingFileHandler as LogHandler
from cloghandler import ConcurrentRotatingFileHandler as LogHandler
import sys, time

logger = logging.getLogger('name')
#formatter = logging.Formatter('%(name)s - %(process)d - %(message)s')
formatter = logging.Formatter('%(message)s')
loghandler = LogHandler('tmp.log', 'a', 1024, 1024*1024*1024)
loghandler.setFormatter(formatter)
logger.addHandler(loghandler)

def log(msg):
    logger.error('log in child: %d' % msg)

try:
    number = sys.argv[1]
except:
    number = 10
number = int(number)

print 'number is %d' % number
oldtime = time.time()
print 'start time %s' % oldtime

l = []
for i in range(number):
    p = P(target=log, args=(i,))
    l.append(p)

with open('tmp.log', 'w') as file:
    file.write('')

map(lambda x:x.start(), l)
logger.error('log in father')

map(lambda x:x.join(), l)
newtime = time.time()
print 'end time %s' % newtime
print 'gap time %s' % (newtime - oldtime)

