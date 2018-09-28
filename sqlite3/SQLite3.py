#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 2:42 PM
# @Author  : liangk
# @Site    : 
# @File    : SQLite3.py
# @Software: PyCharm


import sqlite3


def createTable():

    # 连接数据库，如果不存在，则创建
    conn = sqlite3.connect('test.db')
    # 创建cursor
    cursor = conn.cursor()
    # 执行一条sql语句，创建user表
    # cursor.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('create table if not exists user (id varchar(20), name varchar(20))')
    # 插入数据, id 要改
    cursor.execute('insert into user (id, name) values (\'10\', \'Michael\')')
    # 通过rowcount 获得插入的行数
    row = cursor.rowcount

    # 关闭cursor
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭connection
    conn.close()


def selectTable():

    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # 执行查询语句
    cursor.execute('select * from user where id = ?', ('1'))
    values = cursor.fetchall()
    print(values)

    cursor.execute('select * from user ')
    values1 = cursor.fetchall()
    print(values1)

    cursor.close()
    conn.close()

# 程序主入口
if __name__ == '__main__':

    print('开始连接数据库')
    # sqlite3.OperationalError: table user already exists
    # 说明数据库已经存在了  不需要再创建
    createTable()

    print('查询数据')
    selectTable()
