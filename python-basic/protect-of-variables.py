class P:
    a = 1
    _b = 2
    __c = 3

    def output(self):
        print self.a, self._b, self.__c

class C1(P):
    a = 4
    _b = 5
    __c = 6

    def output2(self):
        print self.a, self._b, self.__c

class C2(P):

    def output(self):
        print self.a, self._b, self.__c

p = P()
c1 = C1()
c2 = C2()

p.output()
c1.output()
c1.output2()
c2.output()
