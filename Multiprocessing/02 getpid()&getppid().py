import os

# getpid() can get the pid of child process, getppid() can get the parent pid
pid = os.fork()

if pid < 0:
    print 'fork() call failed\n'
if pid == 0:
    print '\nThis is the child process(pid = %d), and the parent process is %d' %(os.getpid(), os.getppid())
else:
    print '\nThis is the parent process(pid = %d), and the child process is %d' %(os.getpid(), pid)

print 'They both can print this line'
