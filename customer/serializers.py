#!/usr/bin/env python3
# coding:utf-8

__author__ = '徐育良'


from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_pet_name', 'iphone', 'email', 'password', 'age', 'address','info',)