from socket import *

severSocket = socket(AF_INET, SOCK_STREAM)

severSocket.bind(('',8899))

severSocket.listen(5)

print 'start to listen...'
clientSocket, clientInfo = severSocket.accept()

print 'connect success.'
print 'ready to accept msg.'

recvData = clientSocket.recv(1024)

print 'msg received.'
print '%s: $s'%(str(clientInfo), recvData)

clientSocket.close()
severSocket.close()
