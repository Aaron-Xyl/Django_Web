#!/usr/bin/env python3
# coding:utf-8

__author__ = '徐育良'
import requests

# def test_get_add_use():
#     host = 'http://192.168.0.12:8099/user_manage/insertUser'
#     # host = 'http://192.168.0.4:8000/customer/updata'
#     res = requests.post(host, data={'id': '2', 'user_id': '1', 'user_pet_name': '2', 'iphone': '3', 'email': '4',
#                                     'password': '5', 'age': '6', 'address': '7', 'info': '8'})
#     print(res.text)
#
#     # host = 'http://127.0.0.1:8000/customer/search_data'
#     # res = requests.post(host, data={'id': '1'})
#     # print(res.text)
#
#
# test_get_add_use()

import time, random

user = {'user': None, 'login_time': None, 'timeout': 0.000003, }


def timmer(func):
    def wrapper(*args, **kwargs):
        s1 = time.time()
        res = func(*args, **kwargs)
        s2 = time.time()
        print('%s' % (s2 - s1))

        return res

    return wrapper


def auth(func):
    def wrapper(*args, **kwargs):
        print(user['user'])
        if user['user']:
            timeout = time.time() - user['login_time']
            if timeout < user['timeout']:
                return func(*args, **kwargs)
        name = input('name>>: ').strip()
        password = input('password>>: ').strip()
        if name == 'egon' and password == '123':
            user['user'] = name
            user['login_time'] = time.time()
            res = func(*args, **kwargs)
            return res

    return wrapper


@auth
def index():
    time.sleep(random.randrange(3))
    print('welcome to index')


@auth
def home(name):
    time.sleep(random.randrange(3))
    print('welcome %s to home ' % name)

index()
home('egon')
