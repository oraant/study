class A:
    def f1(self):
        print 'hello1'

    @classmethod
    def f2(cls):
        print 'hello2'

    @staticmethod
    def f3():
        print 'hello3'

a=A()
a.f1()

A.f1()

A.f2()

A.f3()
