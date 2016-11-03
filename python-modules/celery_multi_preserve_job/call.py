from tasks import raiseerror, preserve
from time import sleep
from sys import stdout

r = raiseerror.delay('r', 10)

for i in range(2000):
    sleep(0.01)
    stdout.flush()
    msg = '\r' + r.state + ' ' + r.status
    stdout.write(msg)
    stdout.flush()

print
