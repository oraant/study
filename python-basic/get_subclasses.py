from time import sleep

class A(object):
    print A.__subclasses__()

def get():
    print [ (x.__name__,x.S.name) for x in A.__subclasses__() ]

class B(A):
    class S:
        name='hh'

class C(A):
    class S:
        name='hh'

#for sub in A.__subclasses__():
#    print sub.__name__


A
