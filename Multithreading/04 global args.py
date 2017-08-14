from threading import Thread
import time

global_num = 10

def work1():
    global global_num
    for i in range(3):
        global_num += 1
    print 'in work1: global_num = %d' %global_num

def work2():
    global global_num
    print 'in work2: global_num = %d' %global_num

print 'global_num = %d before create threads' %global_num

t1 = Thread(target=work1)
t1.start()

# make sure Thread-1 is finished
time.sleep(1)

t2 = Thread(target=work2)
t2.start()
