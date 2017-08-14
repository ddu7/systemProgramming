import threading, time

def saySomething():
    print 'I am saying something'
    time.sleep(1)

def sing():
    for i in range(3):
        print '\nsinging'
        time.sleep(1)
def dance():
    for i in range(3):
        print '\ndancing'
        time.sleep(1)


# without threading
if __name__ == '__main__':
    for i in range(5):
        saySomething()

# Use threading
if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=saySomething)
        t.start()

if __name__ == '__main__':
    print '----start----'

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    # though it print end, the main thread won't exist until child thread finished
    print '\n----end----'