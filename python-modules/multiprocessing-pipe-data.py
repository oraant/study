from multiprocessing import Pipe
f, c = Pipe()

msg = {'method':'start', 'arg':['haha', 'hoho']}

f.send(msg)

result = c.recv()
print result
print type(result)
