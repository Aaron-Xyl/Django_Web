#!/usr/bin/env python3
# coding:utf-8

__author__ = '徐育良'

import requests
from functools import wraps
import unittest

POCKET = 'Pocket'
XYL = 'Xyl'


def auto_header(parm=None):
    def w_header(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print(parm)
            kw.update({
                'res_list': parm
            })
            return func(*args, **kw)

        return wrapper

    return w_header


def return_data(func):
    @wraps(func)
    def wrapper(*args, **kw):
        res = func(*args, **kw)
        print('参数返回:===> %s ' % res.text)

    return wrapper


class TestAPIFunctions(unittest.TestCase):
    res_l = [{'url': 'http://192.168.0.4:8000/customer/updata',
                 'param': {'id': '2',
                           'user_id': '1',
                           'user_pet_name': '2',
                           'iphone': '3',
                           'email': '4',
                           'password': '5',
                           'age': '6',
                           'address': '7',
                           'info': '8'},
              'method': 'GET'}]

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @auto_header(res_l)
    @return_data
    def test_self(self, res_list = None):
        for data in res_list:
            url = data.get('url')
            method = data.get('method')
            param = data.get('param')
            if method == 'POST':
                res = requests.post(url, param)
                return res
            else:
                res = requests.get(url, param)
                return res

    def test_other(self):
        pass


if __name__ == '__main__':
    unittest.main()
