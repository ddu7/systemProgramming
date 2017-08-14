# coding: utf-8

import time

def application(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'Text/plain'),
        ('Server', 'My Server')
    ]
    start_response(status, headers)
    return time.ctime()