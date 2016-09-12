a = 1
_a = 2
__a = 3

print a, _a, __a

def f():
    print 'f1'

def _f():
    print 'f2'

def __f():
    print 'f3'

f()
_f()
__f()
