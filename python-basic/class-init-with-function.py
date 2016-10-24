# coding:utf-8

def f():return 1

class C:
    def __init__(self, a=f()):
        self.a = a

    def output(self):
        print self.a

c1 = C()
c2 = C(2)

c1.output()
c2.output()

# 结论
# 参数可以通过方法的返回值来设置默认值
