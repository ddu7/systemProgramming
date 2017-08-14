# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random

def worker(msg):
    t_start = time.time()
    print 'request %s start, process id = %d' %(msg, os.getpid())
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print 'request %s end, running time = %0.2f' %(msg, t_stop - t_start)

# 定义进程池的进程数
po = Pool(3)

for i in range(10):
    # Pool.apply_async(要调用的目标,(传递给目标的参数元组,))
    # 每次循环将会用空闲出来的子进程去调用目标
    po.apply_async(worker, (i,))

print '----start----'
# 关闭进程池，关闭后po不再接收新的请求
po.close()
# 一般用子进程执行实际任务，而主进程用来等待
po.join()
print '----end----'

# multiprocessing.Pool常用函数解析：
#
#   apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），
#                                       args为传递给func的参数列表，kwds为传递给func的关键字参数列表；
#
#   apply(func[, args[, kwds]])：       使用阻塞方式调用func
#
#   close()：                           关闭Pool，使其不再接受新的任务；
#
#   terminate()：                       不管任务是否完成，立即终止；
#
#   join()：                            主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；