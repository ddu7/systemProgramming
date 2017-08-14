import os
import time

num = 0

pid = os.fork()

if pid == 0:
    num += 1
    print 'child process add num by 1, num = %d\n' %num
else:
    time.sleep(1)
    print 'parent process return num, num = %d' %num
    print 'we can see that num value does not change with the child process'