# -*- coding: utf-8 -*-
from threading import Thread
from socket import *

# receive data, and print
def recvData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print '>>%s: %s'%(str(recvInfo[1]), recvInfo[0])

# send data
def sendData():
    while True:
        sendInfo = raw_input('<<')
        udpSocket.sendto(sendInfo.encode('gb2312'), (destIP, destPort))

udpSocket = None
destIP = ''
destPort = 0

def main():
    global udpSocket
    global destIP
    global destPort

    destIP = raw_input('>> Receicer\'s IP: ')
    destPort = int(raw_input('>> Receiver\'s Port: '))

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind('',7777)

    recv = Thread(target=recvData)
    send = Thread(target=sendData)

    recv.start()
    send.start()

    recv.join()
    send.join()

if __name__ == '__main__':
    main()
