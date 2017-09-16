#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.forms import Form
from django.forms import fields

class LoginForm(Form):
    username = fields.CharField(
        required=True,
        error_messages={'required': '用户名不能为空!'},
    )
    password = fields.CharField(
        required=True,
        error_messages={'required': '密码不能为空!'},
    )


class RegisterForm(Form):
    username = fields.CharField(
        required=True,
        error_messages={'required': '用户名不能为空!'},
    )
    password = fields.CharField(
        required=True,
        min_length=6,
        error_messages={'required': '密码不能为空!', 'min_length': "密码不能小于6个字符"},
    )
    password_retry = fields.CharField(
        required=True,
        error_messages={'required': '确认密码不能为空!'},
    )
    email = fields.EmailField(
        required=True,
        error_messages={'required': '邮箱不能为空!', 'invalid': '邮箱格式错误'},
    )

class ModifyForm(Form):
    hostname = fields.CharField(
        required=True,
        error_messages={'required':'主机名不能为空！'}
    )
    ip = fields.GenericIPAddressField(
        required=True,
        error_messages={'required':'IP不能为空！','invalid':'IP格式错误'}
    )
    port = fields.IntegerField(
        required=True,
        max_value=65535,
        min_value=1,
        error_messages={'required':'端口为非空数字,范围1-65535!',}
    )

class ServiceForm(Form):
    name = fields.CharField(
        required=True,
        error_messages={'required': '业务线名不能为空!'}
    )

