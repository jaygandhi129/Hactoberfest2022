from threading import *
from time import sleep

class Demo1(Thread):
    def run(self):
        for i in range(15):
            print("Demo1")
            #to introduce time gap between two threads
            sleep(0.5)

class Demo2(Thread):

    def run(self):
        for i in range(15):
            print("Demo2")
            sleep(0.5)

t1=Demo1()
t2=Demo2()

t1.start()
#to introduce time gap and avoid both threads reaching CPU at same time
sleep(0.2)
t2.start()
#to execute bye after t1 and t2 threads as bye is executed by main thread
t1.join()
t2.join()

print("Bye")


