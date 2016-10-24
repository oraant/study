import logging

# set logger
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formater = logging.Formatter('%(asctime)s - %(module)s - %(funcName)s - %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formater)
handler.setLevel(logging.DEBUG)

log = logging.getLogger('hello')
log.addHandler(handler)

# create class
class C:
    def __init__(self, logger):
        self.logger = logger
        self.logger.name = 'hello.world'
    def output(self, msg):
        self.logger.info(msg)
        print '--- %d' % id(self.logger)

# test log
c = C(log)

log.info('haha')
print '--- %d' % id(log)
c.output('hehe')

# 结论：
# 一个logger传给别人后，只要改名字，全局的名字就都变了
