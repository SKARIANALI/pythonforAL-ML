from threading import *
from time import *

class A(Thread):
 def run(self): #run() predefined method in threading
  for i in range(5):
   print("Akhilesh")
   sleep(1)

class B(Thread):
 def run(self):
  for i in range(5):
   print("Ankush")
   sleep(1)

t1 = A()
t2 = B()

#t1.run()
#t2.run()

t1.start() # start() to acheive multhreading instead of calling run() # also called the run() behind the scene  
t2.start()

t1.join()
t2.join()

print("Ankit")

'''Synchronization: When you call t1.join(), the main thread (the program itself) 
will wait for the thread t1 to finish 
its task before continuing with the rest of the code '''


import threading

def show():
    for i in range(3):
        print("Hello")

t = threading.Thread(target=show)

t.start()
t.join()

print("Done")


import threading
import time

def task1():
    for i in range(5):
        print("Task 1")
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2")
        time.sleep(1)

# create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# start threads
t1.start()
t2.start()

# wait until threads finish
t1.join()
t2.join()

print("Program End")