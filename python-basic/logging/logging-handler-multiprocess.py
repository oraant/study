import logging
from time import sleep
from multiprocessing import Process

# set logger
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formater)
handler.setLevel(logging.DEBUG)


# create class
class C:
    def __init__(self, handler):
        self.logger = logging.getLogger('hello.world')
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
    def output(self, msg):
        self.logger.info(msg)
        print self.logger.handlers

def new_process():
    c = C(handler)
    c.output('p - aaa')
    sleep(1)
    c.output('p - bbb')
    
log = logging.getLogger('hello')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

log.info('f - aaa')
Process(target=new_process).start()
sleep(2)
log.info('f - bbb')
