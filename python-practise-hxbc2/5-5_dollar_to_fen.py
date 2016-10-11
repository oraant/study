def get_result(dollar=None):

    if not dollar:
        from random import randrange as rr
        fen = rr(1,101)
    else:
        fen = dollar * 100

    print "fen is %s" % fen

    c25 = fen // 25
    y25 = fen % 25

    if y25:
        c10 = y25 // 10
        y10 = y25 % 10

    if y10:
        c5 = y10 // 5
        y5 = y10 % 5

    print '25 : %d\n10 : %d\n05 : %d\n01 : %d' % (c25, c10, c5, y5)

