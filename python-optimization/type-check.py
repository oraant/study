# author:oraant

from time import time
import types

# compare different way to check type,ref is <<Python Core Program>>

def f1(num):
    if isinstance(num, int): #2.5s
        pass

def f2(num):
    if num is types.IntType: #2s
        pass

def f3(num):
    if type(num) == types.IntType: #3s
        pass

def f4(num):
    if type(num) == type(3): #3s
        pass

for f in f1,f2,f3,f4:
    old=time()
    for i in range(10000000): f(99)
    print f.__name__, time()-old
