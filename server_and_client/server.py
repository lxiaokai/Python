#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 5:04 PM
# @Author  : liangk
# @Site    : 
# @File    : server.py
# @Software: PyCharm


import socket
import threading
import time


# 以下是每次TCP连接将要执行的线程
def tcplink(sock, addr):
    print('新连接 %s:%s...' % addr)
    sock.send(b'Greating from MacPro PC server!')
    while True:
        data = sock.recv(1024)  # For this session, pause here, once client socket send message proceed following:
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听Localhost端口
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        sock, addr = s.accept()  # Paused here, once received connection proceed the following:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
