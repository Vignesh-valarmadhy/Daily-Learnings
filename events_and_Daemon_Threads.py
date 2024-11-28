import threading

event = threading.Event()

def myfunc():
    print('Waiting for event to trigger ......\n')
    event.wait()
    print("Performing action x y Z")

t1 = threading.Thread(target=myfunc)
t1.start()

x = input("do you want to trigger the event (y/n) \n")
if x == "y":
    event.set()
else:
    event.clear()