# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import requests
import time
import re
# Create your views here.

def login(request):
    ctime=time.time()*1000
    login_url="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}".format(ctime)
    response=request.get(login_url)
    result=re.findall('window.QRLogin.uuid=(.*);',response.text)
    qcode=result[0] if result else ""
    request.session['qcode']=qcode
    request.session['ctime']=ctime
    return render(request,'login.html',{"qcode":qcode})