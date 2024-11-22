import threading 

# def helloworld():
#     print("hello world")

# t1 = threading.Thread(target=helloworld)
# t1.start()

def function1():
    for x in range(10):
        print("One")

def function2():
    for x in range(10):
        print("Two")


# function1() # without threading first function1 is executed 
# function2() # then the function2 is executed 

# no parallel execution is possible

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()
t1.join() # waits for t1 thread to finish 
t2.join() # waits for t2 thread to finish

print("Another Text")