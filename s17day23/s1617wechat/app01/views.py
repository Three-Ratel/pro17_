from django.shortcuts import render,HttpResponse
import requests
import re
import time

# Create your views here.

def login(req):
    ctime=time.time()*1000
    qcode_url = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}".format(ctime)
    r1=requests.get(qcode_url)
    # print(r1.text)#获取图片地址的后缀   window.QRLogin.code = 200; window.QRLogin.uuid = "gc8KHu2Yng==";
    data = re.findall('uuid = "(.*)";', r1.text)
    qcode=data[0]
    print(qcode)
    return render(req, 'login.html',{'qcode':qcode})
def check_login(req):
    #r1=requests.get('微信检测用户扫码url')
    #如果r1.text,包含window=408 表示用户三十秒未扫码
    #如果包含302则表示已经扫码,把用户头像返回
    #如果包含200,表示用户已经扫码,点击确认登录
    #r1.text
    time.sleep(10)
    return HttpResponse('...')