#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 5:11 PM
# @Author  : liangk
# @Site    : 
# @File    : client.py
# @Software: PyCharm

import socket

# 程序主入口
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    print('开始发送数据')
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
