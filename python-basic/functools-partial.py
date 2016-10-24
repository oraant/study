from functools import partial

class C:

    def __init__(self):
        self.haha = partial(self.output, msg='haha')
        self.hehe = partial(self.output, msg='hehe')

    def output(self, msg):
        print msg



c = C()
c.haha()
c.hehe()
c.output('wow')
