import warnings as w

s=['th','he']

w.filterwarnings("ignore", '|'.join(s))
#w.filterwarnings("ignore", "he")
print '|'.join(s)

w.warn("hello")
w.warn("this")
w.warn("is")
w.warn("me")
