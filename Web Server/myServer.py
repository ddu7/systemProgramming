# coding: utf-8
import socket
from multiprocessing import Process
import re
import sys

# 设置静态文件根目录
HTML_ROOT_DIR = './html'
WSGI_PYTHON_DIR = './wsgipy'

class HTTPServer(object):
    """"""
    def __init__(self, application):
        '''application指的是框架内的app'''
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app = application

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print '用户[%s];端口[%s] 连接上了。' % client_addr
            handler = Process(target=self.handle_client, args=(client_socket,))
            handler.start()
            client_socket.close()

    def start_response(self, status, headers):
        '''
        status = '200 OK'
        headers = [
        ('Content-Type', 'Text/plain')
        ]
        '''
        response_headers = 'HTTP/1.1' + status + '\r\n'
        for header in headers:
            response_headers += '%s: %s \r\n' %header
        self.response_headers = response_headers

    def handle_client(self, client_socket):
        '''处理客户端请求'''
        # 获取客户端请求数据
        recvData = client_socket.recv(1024)

        # 解析请求报文, 提取用户请求文件名
        request_lines = recvData.splitlines()
        request_start_line = request_lines[0]
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line).group(1)
        method = re.match(r"(\w+) +/[^ ]*", request_start_line).group(1)

        env = {
            'PATH_INFO': file_name,
            'METHOD': method
        }
        response_body = self.app(env, self.start_response)

        response = self.response_headers + '\r\n' + response_body

        # 返回响应数据
        client_socket.send(response)

        # 关闭套接字，结束通讯
        client_socket.close()

    def bind(self, port):
        self.server_socket.bind(('', port))

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    if len(sys.argv) < 2:
        sys.exit('python MyServer.py Module:app')

    # python myServer.py myWebFramework:app
    module_name, app_name = sys.argv[1].split(':')
    m = __import__(module_name)
    app = getattr(m, app_name)

    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start()

if __name__ == '__main__':
    main()