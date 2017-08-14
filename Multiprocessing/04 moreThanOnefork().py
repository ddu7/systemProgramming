import os
import time

pid = os.fork()
if pid == 0:
    print 'This is fork1-child.'
else:
    print 'This is fork1-parent.'

time.sleep(1)

pid = os.fork()
if pid == 0:
    print 'This is fork2-child.'
else:
    print 'This is fork2-parent.'


# The order of each process is totally depend on the os's scheduling algorithm.
