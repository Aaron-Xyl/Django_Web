#!/usr/bin/env python3
# coding:utf-8

__author__ = '徐育良'
from django.http import JsonResponse

Param_miss = JsonResponse({'code': 601, 'msg': '参数缺失'})
User_name_long = JsonResponse({'code': 600, 'msg': '用户名太长'})
password_error = JsonResponse({'code': 602, 'msg': '密码错误'})
No_user_id = JsonResponse({'code': 603, 'msg': '用户不存在'})
user_id_error = JsonResponse({'code': 604, 'msg': '请输入字母和数字结合的用户名'})
enter_user_id = JsonResponse({'code': 605, 'msg': '请输入用户名'})
iphone_error = JsonResponse({'code': 606, 'msg': '请输入正确的手机号码'})
iphone_digit = JsonResponse({'code': 607, 'msg': '请输入数字'})
iphone_null = JsonResponse({'code': 608, 'msg': '手机号码为空'})
email_error = JsonResponse({'code': 609, 'msg': '邮箱名错误'})
email_null = JsonResponse({'code': 610, 'msg': '邮箱为空'})
password_inv = JsonResponse({'code': 611, 'msg': '密码无效，长度超过16或者短于8'})
password_inv_str = JsonResponse({'code': 612, 'msg': '密码包含无效字符'})
