# -*- coding: utf-8 -*-
from socket import *
from multiprocessing import *

def service(newSocket, clientAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print 'recv[%s]: %s'%(str(clientAddr), recvData)
        else:
            print '[%s]客户端已关闭'%str(clientAddr)
            break
    newSocket.close()


def main():
    serSocket = socket(AF_INET, SOCK_STREAM)

    # 重复使用绑定信息，这样即使服务器需要2MSL也可以重复绑定端口
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    localAddr = ('', 7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)

    try:
        while True:
            print ' ---主进程，等待客户端---'
            newSocket, clientAddr = serSocket.accept()

            print '---创建新进程处理客户端请求---'
            clientSocket = Process(target=service, args=(newSocket, clientAddr))
            clientSocket.start()

            # 已经向子进程复制了一份， 父进程中newSocket也没用了
            newSocket.close()
    finally:
        serSocket.close()

if __name__ == '__main__':
    main()