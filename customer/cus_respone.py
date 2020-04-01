#!/usr/bin/env python3
# coding:utf-8

__author__ = '徐育良'
from django.http import HttpResponse
import json


class CusReturn(object):
    content_type = 'application/json'

    def __str__(self):
        return "content_type = 'application/json'"


class CusHttpRespone(HttpResponse):
    def __init__(self, result, content_type='application/json', *args, **kwargs):
        super(CusHttpRespone, self).__init__(content_type=content_type, *args, **kwargs)
        self.content = json.dumps(result)
