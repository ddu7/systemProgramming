import threading, time

class newThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)

            # default name of thread name is Thread-n
            print 'I am ' + self.name + ' @ ' + str(i)

t = newThread()
t.start()