import logging


# create class
class B:

    def __init__(self):

        #self.logger = logging.getLogger(__name__)
        self.logger = logging.getLogger()

    def output(self, msg):
        self.logger.info(msg)
        #print self.logger.handlers
