#!/usr/bin/python
# -*- coding:utf-8 -*-

import hashlib
#存密码的时候
def make_md5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    data = obj.hexdigest()
    return data
