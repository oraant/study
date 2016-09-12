# coding:utf-8

haha = False

def log(func):

    def wrapper(*args, **kw):
        global haha
        if haha:
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        else:
            print 'no'

    return wrapper

@log
def sayhi(msg):
    print 'hello', msg


haha = True
sayhi('qiao')

haha = False
sayhi('qiao')
