# -*- coding: utf-8 -*-
from multiprocessing import Process
import time, os

# 继承Precess类
class newProcess(Process):
    # 重写__init__方法，可以直接将继承类本身传递给Process.__init__来完成初始化
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    # start() 会调用 run() 方法
    def run(self):
        print 'child process %s start, parent process is %s ' %(os.getpid(), os.getppid())
        s_time = time.time()
        time.sleep(self.interval)
        e_time = time.time()
        print 'process %s end, running rime = %0.2f' %(os.getpid(), e_time - s_time)

if __name__ == '__main__':
    t_start = time.time()
    print 'current process pid = %s' % os.getpid()
    p1 = newProcess(2)
    p1.start()
    p1.join()
    t_end = time.time()
    print 'process %s end, running rime = %0.2f' % (os.getpid(), t_end - t_start)