# -*- coding: utf-8 -*-
import threading
import time

def test():
    name = threading.current_thread().name
    print '---current thread name is: %s---' %name
    g_num = 100
    if name == 'Thread-1':
        g_num += 1
    else:
        time.sleep(1)
    print '---thread is %s, num = %d' %(name, g_num)

p1 = threading.Thread(target=test)
p1.start()

p2 = threading.Thread(target=test)
p2.start()

# 在多线程开发中，全局变量是多个线程都共享的数据，而局部变量等是各自线程的，是非共享的
