from socket import *

tcpServerSocket = socket(AF_INET, SOCK_STREAM)

addrs = ('', 8899)
tcpServerSocket.bind(addrs)

tcpServerSocket.listen(5)

while True:
    newSocket, clientAddr = tcpServerSocket.accept()

    while True:
        recvData = newSocket.recv(1024)

        if len(recvData) > 0:
            print '>>Receive: '
        else:
            break

        sendData = raw_input('>>Send back: ')
        newSocket.send(sendData)

    newSocket.close()

tcpServerSocket.close()
