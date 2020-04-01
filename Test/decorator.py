#!/usr/bin/env python3
# coding:utf-8

__author__ = '徐育良'

import time
from functools import wraps

# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         time.sleep(3)
#         stop = time.time()
#         print('执行时间是%s' % (stop - start))
#
#     return wrapper
#
#
# @timmer
# def exe():
#     print('你愁啥！')
#
#
# exe()

user_dict = {'123': '321', '456': '654', '789': '987'}
current_user = {'name': ''}


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user['name']:
            func(*args, **kwargs)
        else:
            name = input('输入名称: ')
            password = input('输入密码: ')
            print(user_dict['123'])
            if name in user_dict.keys() and password in user_dict.values():
                func(*args, **kwargs)
                current_user['name'] = name
            else:
                print('  ⊙︿⊙  name or password error')

    return wrapper


# @auth
# def login(name=''):
#     print('Hello, %s, welcome!' % name)
#
#
# login()
@auth
def my_log():
    print('this is my_log')


@auth
def my_name():
    print('欢迎登陆')


my_log()
my_name()
