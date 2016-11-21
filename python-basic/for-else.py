# for i in range(5):
#     print i
# else:
#     print 9

def f():
    for i in range(5):
        if i > 2:
            print 'in'
            return i
    print 'after'
    return 9

print f()
