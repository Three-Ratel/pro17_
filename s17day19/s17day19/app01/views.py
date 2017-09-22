from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils import md5
import datetime

#用装饰器 可以不用每个views都写获取session
def auth(func):
    def inner(request,*args,**kwargs):
        ck = request.session.get('yyyyyyyy')
        print(ck)
        if not ck:
            return redirect('/login.html')
        return func(request,*args,**kwargs)
    return inner

# Create your views here.
def index(request):
    # 获取cookie
    # ck = request.COOKIES.get('uuuuuuuu')

    # 获取session
    ck = request.session.get('yyyyyyyy')
    print(ck)
    if not ck:
        return redirect('/login.html')
    user=request.session.get('yyyyyyyy')
    return render(request,'index.html',{'user':user})

@auth
def order(request):
    return HttpResponse('订单列表' )

def login(request):
    if request.method == "GET":
        return render(request, 'login.html', locals())
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        pwd = md5.encrypt(pwd)
        obj = models.UserInof.objects.filter(username=user, password=pwd).first()
        # if user == 'alex' and pwd == '123':
        if obj:
            # #添加cookie
            # response=redirect('/index.html')
            # deadline=datetime.datetime.utcnow() +datetime.timedelta(seconds=5)
            # response.set_cookie('uuuuuuuu',user,expires=deadline,path='/')
            # return response

            # session
            # 生成随机字符串
            # cookie发送给客户端
            # 服务端随机字符串为key  自己设置一些value
            request.session['yyyyyyyy'] = user
            return redirect('/index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
def logout(request):
    request.session.clear()
    return redirect('/index.html')