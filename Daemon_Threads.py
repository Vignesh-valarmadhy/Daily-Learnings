import threading
import time

path = "text.txt"
text = ""

def read_file():
    global path , text
    while True:
        with open("text.txt","r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=read_file,daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()

# so this daemon threads actually reads the textfile as there is even continous update going on 

