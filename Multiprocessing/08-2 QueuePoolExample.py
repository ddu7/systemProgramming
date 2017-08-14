#coding=utf-8

# 如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()
# 否则会错误信息：
#   RuntimeError: Queue objects should only be shared between processes through inheritance.

from multiprocessing import Manager, Pool
import os

def read(q):
    print 'start read on process %s. parent process is %s.' %(os.getpid(), os.getppid())
    while not q.empty():
        print 'read data: %s' %q.get(True)
    print 'read end'

def write(q):
    print 'start write on process %s, parent process is %s' %(os.getpid(), os.getppid())
    for value in 'DATA':
        print 'write data: %s' %value
        q.put(value)
    print 'write end'

if __name__ == '__main__':
    print '----start----'
    print 'start process: %s' %os.getpid()
    q = Manager().Queue()
    pool = Pool()
    # 使用阻塞式， write完成之后才能read
    pool.apply(write, (q,))
    pool.apply(read, (q,))
    pool.close()
    pool.join()
    print '----end----'