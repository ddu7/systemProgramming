from multiprocessing import Process
import os, time

def runProcess(name, age, **kwargs):
    for i in range(10):
        print 'child process running, name = %s, age = %d, pid = %d' %(name, age, os.getpid())
        print kwargs
        time.sleep(0.5)

if __name__=='__main__':
    print 'parent process is pid = %d' %os.getpid()
    p = Process(target= runProcess, args=('test', 18), kwargs={'m':20})
    print 'child process start'
    p.start()
    time.sleep(1.5)
    p.terminate()
    p.join()
    print 'child process stop'
