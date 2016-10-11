def get_years(start=0, end=3000):
    l=[]
    for y in range(start, end):
        if y%100 == 0 and y%400 == 0:
            l.append(y)
        elif y%100 != 0 and y%4 == 0:
            l.append(y)
    return l

print get_years()
