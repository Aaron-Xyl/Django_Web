#!/usr/bin/env python3
# coding:utf-8

__author__ = '徐育良'

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 接受的规则，接收来源，命名
    path('add_data', views.add_data, name='add_data'),
    path('delete_data', views.delete_data, name='delete_data'),
    path('search_data', views.search_data, name='search_data'),
    path('updata', views.updata, name='updata'),
]
