class C:
    def __init__(self):
        raise StandardError('haha')
    def output(self, msg):
        print msg

class P:
    def __init__(self):
        #c = C()
        return 'lala'
    def output(self, msg):
        print msg


print '---'
b = P()
print '---'
b.output('hehe')
print '---'
