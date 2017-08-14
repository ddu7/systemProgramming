# -*- coding: utf-8 -*-
from multiprocessing import Process
import time, os

def worker_1(interval):
    print 'worker_1, parent process = %s, current process = %s' %(os.getppid(), os.getpid())
    start_time = time.time()
    time.sleep(interval)
    end_time = time.time()
    print 'worker_1, running time = %0.2f sec' %(end_time - start_time)

def worker_2(interval):
    print 'worker_2, parent process = %s, current process = %s' %(os.getppid(), os.getpid())
    start_time = time.time()
    time.sleep(interval)
    end_time = time.time()
    print 'worker_2, running time = %0.2f sec' %(end_time - start_time)

print 'current process pid = %s' %os.getpid()

# 创建两个进程对象，target指向这个进程对象要执行的对象名称，
# args后面的元组中，是要传递给worker_1方法的参数，
# 因为worker_1方法就一个interval参数，这里传递一个整数2给它，
# 如果不指定name参数，默认的进程对象名称为Process-N，N为一个递增的整数
p1 = Process(target=worker_1, args=(2,))
p2 = Process(target=worker_2, name = 'Test',args=(1,))

# 使用"进程对象名称.start()"来创建并执行一个子进程，
# 这两个进程对象在start后，就会分别去执行worker_1和worker_2方法中的内容
p1.start()
p2.start()

# 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
print("p2.is_alive = %s"%p2.is_alive())

print("p1.name = %s" %p1.name)
print("p1.pid = %s" %p1.pid)
print("p2.name = %s" %p2.name)
print("p2.pid = %s" %p2.pid)


# join括号中不携带参数，表示父进程在这个位置要等待p1进程执行完成后，再继续执行下面的语句，
# 一般用于进程间的数据同步，如果不写这一句，下面的is_alive判断将会是True
# 如果将下面的这条语句改成p1.join(1)，因为p2需要2秒以上才可能执行完成，父进程等待1秒很可能不能让p1完全执行完成，
# 所以下面的print会输出True，即p1仍然在执行
p1.join()
print("p1.is_alive = %s" %p1.is_alive())