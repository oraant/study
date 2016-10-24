import logging
from model_b import B
from multiprocessing import Process

# set logger


# create class
class A:

    def __init__(self):

        formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formater = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

        handler = logging.StreamHandler()
        handler.setFormatter(formater)
        handler.setLevel(logging.DEBUG)

        self.logger = logging.getLogger()
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def output(self, msg):
        self.logger.info(msg)
        #print self.logger.handlers

def print_a():
    a = A()
    a.output('this is a')

def print_b():
    b = B()
    b.output('this is b')

print_b()
print_a()
print_b()
Process(target=print_b).start()
