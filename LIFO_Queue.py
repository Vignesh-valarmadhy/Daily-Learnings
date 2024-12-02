import queue

q = queue.LifoQueue()
number = [1,2,3,4,5,5,6,7]

for i in number:
    q.put(i)

print(q.get())