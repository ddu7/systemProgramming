# -*- coding: utf-8 -*-

# 再不用多线程多进程的情况下设计非堵塞式服务器
from socket import *


# 1. 创建Socket
serSocket = socket(AF_INET, SOCK_STREAM)

# 重复使用绑定信息，这样即使服务器需要2MSL也可以重复绑定端口
serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 2.绑定地址信息： IP和Port
localAddr = ('', 7788)
serSocket.bind(localAddr)

# 3. 将该socket变为非堵塞式
serSocket.setblocking(False)

# 4. 将Socket变为被动监听模式
serSocket.listen(5)

# 保存所有已经连接的客户端，否则在接受一个断开，由于其他都使用同一个引用，会全部被销毁
clientAddrList = []

while True:
    try:
        # 等待客户端到来，三次握手
        clientSocket, clientAddr = serSocket.accept()
    except:
        pass
    else:
        print '一个新的客户端的到来: %s'%(str(clientAddr))
        clientSocket.setblocking(False)
        clientAddrList.append((clientSocket, clientAddr))

    for clientSocket, clientAddr in clientAddrList:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData) > 0:
                print '[%s]: %s'%(str(clientAddr), recvData)
            else:
                clientSocket.close()
                clientAddrList.remove((clientSocket, clientAddr))
                print '%s 已下线'%str(clientAddr)


