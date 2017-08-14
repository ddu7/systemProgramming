import threading, time

class newThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            # default name of thread name is Thread-n
            print 'I am ' + self.name + ' with index ' + str(i)

def test():
    for i in range(5):
        t = newThread()
        t.start()

if __name__ == '__main__':
    test()
