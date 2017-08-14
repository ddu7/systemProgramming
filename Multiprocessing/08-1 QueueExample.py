#coding=utf-8
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for value in ['A', 'B', 'C']:
        print 'put %s into queue' %value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while not q.empty():
        value = q.get(True)
        print 'get %s form queue' %value
        time.sleep(random.random())

if __name__ == '__main__':
    print '----start----'
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print '----end---'
