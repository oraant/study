#!/usr/bin/python
def f1():
    """ different between 'Exception as e' and 'Exception,e' """
    d=[1,2,3]
    try:
        print d[4]
    except Exception as e:
    #    print Exception
        print '---'
        print e

def f2():
    """ close in finally will raise an error """
    try:
        fh = open("testfile", "w")
        print 'open done'

        fh.write("asdfasdfasdf")
        print 'write done'

    except IOError:
        print "Errorsss"

    else:
        print "success"
        fh.close()

f2()
