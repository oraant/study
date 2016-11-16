# coding:utf-8

def f1(msg):
    try:
        exec(msg)
    except:
        print 'excepted'
    else:
        print 'else'
    finally:
        print 'finally'

def f2(msg):
    try:
        exec(msg)
    except:
        print 'excepted'
        raise
    else:
        print 'else'
        return 13
    finally:
        print 'finally'

print '------'
f1('a=1')
print '------'
f1('a')
print '------'
print f2('a=1')
print '------'
print f2('a')

# 结论：
# else和except一样，即便return或者raise了，也会在最后执行finally
print '------'
