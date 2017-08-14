from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

# input the sever's IP address
clientSocket.connect(('ip_address', 8899))

send_msg = raw_input('>>msg: ')
clientSocket.send(send_msg)

recvData = clientSocket.recv(1024)
print 'Receive: $s'%(recvData)

clientSocket.close()


