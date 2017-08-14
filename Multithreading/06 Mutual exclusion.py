# -*- coding: utf-8 -*-
from threading import Thread, Lock
import time

g_num = 0

# test1线程和test2线程都在抢着进行上锁，如果有一方成功的上锁，那么另一方会堵塞（一直等待）到这个锁被解开为止
def test1():
    global g_num
    # lock
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    # unlock
    mutex.release()
    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    # 用来对mutex指向的这个锁进行解锁，只要开了锁，那么接下来会让所有因为这个锁被上了锁而堵塞的线程进行抢着上锁
    mutex.release()
    print("---test2---g_num=%d"%g_num)

# create a lock, it is not locked in default.
mutex = Lock()

# for test1() and test2(), which one lock first, the other one will wait until unlocked.
p1 = Thread(target=test1)
p1.start()

# time.sleep(3)

p2 = Thread(target=test2)
p2.start()

# 当一个线程调用锁的acquire()方法获得锁时，锁就进入“locked”状态。
# 每次只有一个线程可以获得锁。如果此时另一个线程试图获得这个锁，该线程就会变为“blocked”状态，称为“阻塞”，
# 直到拥有锁的线程调用锁的release()方法释放锁之后，锁进入“unlocked”状态。
#
# 线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。
#
# 总之：
# 确保了某段关键代码只能由一个线程从头到尾完整地执行
#
# 阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
# 由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁
