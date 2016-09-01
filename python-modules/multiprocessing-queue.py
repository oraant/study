from multiprocessing import Queue

q = Queue()
q.put('hello1')
q.put('hello2')
print q.get(True)
print q.get(True)

# 队列可以自存自取
# 队列遵循先进先出
