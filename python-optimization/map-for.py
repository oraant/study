from time import time

l=[10000]*1000

def f1():
    [x**x for x in l]

def f2():
    map(lambda x:x**x, l)

def gap(x):
    old_time = time()
    x()
    gap_time = time()-old_time
    print gap_time
    return gap_time
    

a1 = gap(f1)
a2 = gap(f2)
value = abs(a2-a1)/max(a1,a2)*100
print '%2.2f%%' % value
