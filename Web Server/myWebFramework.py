# coding: utf-8
from myServer import HTTPServer, HTML_ROOT_DIR
import time

class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get('PATH_INFO','/')
        # 补充获得静态文件
        if path.startswith('/static'):
            # 访问静态文件
            file_name = path[7:]
            if '/' == file_name:
                file_name = '/index.html'
            try:
                file = open(HTML_ROOT_DIR + file_name, 'rb')
            except IOError:
                status = '404 Not Found'
                headers = []
                start_response(status, headers)
                return 'not found'
            else:
                file_data = file.read()
                file.close()
                # 构造响应数据
                status = '200 OK'
                headers = [
                    ('Server', 'My Server')
                ]
                start_response(status, headers)
                return file_data

        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)
        status = '404 Not Found'
        headers = []
        start_response(status, headers)
        return 'not found'

def show_time(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'Text/plain'),
        ('Server', 'My Server')
    ]
    start_response(status, headers)
    return time.ctime()

def say_hello(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'Text/plain'),
        ('Server', 'My Server')
    ]
    start_response(status, headers)
    return 'Hello from myWebFramework !'

urls = [
    ('/ctime', show_time),
    ('/sayhello', say_hello)
]
app = Application(urls)


# if __name__ == '__main__':
#     urls = [
#         ('/ctime', show_time),
#         ('/sayhello', say_hello)
#     ]
#
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()