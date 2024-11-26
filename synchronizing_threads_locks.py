import threading
import time

x = 8192
lock = threading.Lock()

def double():
    global x,lock
    lock.acquire()
    while x < 16384:
        x *= 2
        time.sleep(1)
    print("Thread 1 has locked the resource")
    print("Reached Maximum")
    lock.release()

def halve():
    global x,lock
    lock.acquire()
    while x >= 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Thread 2 has locked the resource")
    print("Reached the minimum")
    lock.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()
     