# coding:utf-8

class F:

    def log(func):
        def wrapper(*args, **kw):
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        return wrapper

    @log
    def sayhi(self,msg):
        print 'hello', msg

class C(F):
    def sayhi(self,msg):
        print 'wow', msg

f=F()
f.sayhi('qiao')

c=C()
c.sayhi('child')

# 结论：
# wrapper函数可以叫任何名字
# 继承时，复写的话必须得在子类中手动加装饰器
