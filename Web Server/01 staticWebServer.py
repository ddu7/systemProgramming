# coding: utf-8
from multiprocessing import Process
import socket

HTML_ROOT_DIR = ''

def handle_client(client_socket):
    '''处理客户端请求'''
    recvData = client_socket.recv(1024)
    print recvData
    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_headers = 'Server: My Server\r\n'
    response_body = 'Hello World'
    response = response_start_line + response_headers + '\r\n' + response_body
    print 'respose data: ' + response
    client_socket.send(response)
    client_socket.close()

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 8888))
    server_socket.listen(128)


    while True:
        client_socket, client_addr = server_socket.accept()
        print '用户[%s];端口[%s] 连接上了。'%client_addr
        handler = Process(target=handle_client, args=(client_socket,))
        handler.start()
        client_socket.close()