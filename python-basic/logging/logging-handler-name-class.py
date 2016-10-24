import logging

# set logger
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create class
class C:
    def __init__(self):
        self.logger = logging.getLogger('hello.world')
    def output(self, msg):
        self.logger.info(msg)
        print self.logger.handlers

# test log
c = C()

c.output('hehe')

handler = logging.StreamHandler()
handler.setFormatter(formater)
handler.setLevel(logging.DEBUG)

log = logging.getLogger('hello')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

log.info('haha')
log.info('haha')

c.output('hehe')
