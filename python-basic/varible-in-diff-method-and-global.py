# coding:utf-8

class C:

    def f1(self):
        global v
        v = 1

    def f2(self):
        print v

c=C()
c.f1()
c.f2()
print v
