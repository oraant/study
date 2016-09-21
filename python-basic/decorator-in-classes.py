from functools import wraps

class myclass:
    def __init__(self):
        self.start = False

    def _with_check(f):
        @wraps(f)
        def wrapped(inst, *args, **kwargs):
            if inst.check():
                return
            return f(inst, *args, **kwargs)
        return wrapped

    def check(self):
        return self.start

    @_with_check
    def doA(self):
        print('A')

    @_with_check
    def doB(self):
        print('B')