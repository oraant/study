class C:

    var = 0

    def change_var(self, value):
        self.var = value

    def output_var(self):
        print self.var

    def change_cls(self, value):
        self.__class__.var = value

    def output_cls(self):
        print self.__class__.var

a = C()
print 'init var of a is', a.var

a.change_var(1)
print 'after change_var(1), a.var is', a.output_var()
print 'after change_var(1), C.var is', a.output_cls()


a.change_cls(2)
print 'after change_cls(2), a.var is', a.output_var()
print 'after change_cls(2), C.var is', a.output_cls()

b = C()
print 'init var of b is', b.var
