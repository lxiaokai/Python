#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 5:52 PM
# @Author  : liangk
# @Site    : 
# @File    : test25.py
# @Software: PyCharm


import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
# 发送附件引入
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
from_addr = 'xxxxxxx@qq.com'
# 邮箱密码换成他提供的16位授权码
password = 'xxxxxxxxxx'
# 输入收件人地址:可以是一个数组list
to_addr = 'xxxxxx@qq.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 发送文本 第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'
msg = MIMEText('hello,send by python...', 'plain', 'utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# 的收件人的名字很可能不是我们传入的管理员，因为很多邮件服务商在显示邮件时，
# 会把收件人名字自动替换为用户注册的名字，但是其他收件人名字的显示不受影响。
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

'''
# 发送html邮件:
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
'''

'''
# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'html', 'utf-8'))


# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('pic0.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，jpg:
    mime = MIMEBase('image', 'jpg', filename='pic0.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='pic0.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                        '<p><img src="cid:0"></p>' +
                        '</body></html>', 'html', 'utf-8'))

'''

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
