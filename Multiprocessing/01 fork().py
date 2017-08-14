import os


# Attention, fork() function can only be run on Linux/Unix/Mca, cannot run on Win
pid = os.fork()

# the ford() function return 2 times
if pid == 0:
    print 'This is the child process'
    print 'The return value of fork() is %d' %pid
    print 'The return value always is 0\n'
else:
    print 'This is the parent process'
    print 'The return value of fork() is %d' %pid
    print 'The return value is the pid of child process\n'


