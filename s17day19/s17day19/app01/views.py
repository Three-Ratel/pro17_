from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils import md5
from utils.pagination import Page
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# 装饰器:csrf_exempt指定某个视图函数不使用
# 装饰器:csrf_protect 指定某个视图函数使用,默认全站不启用

import datetime


# 用装饰器 可以不用每个views都写获取session
def auth(func):
    def inner(request, *args, **kwargs):
        ck = request.session.get('yyyyyyyy')
        print(ck)
        if not ck:
            return redirect('/login.html')
        return func(request, *args, **kwargs)

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
    user = request.session.get('yyyyyyyy')
    return render(request, 'index.html', {'user': user})


@auth
def order(request):
    return HttpResponse('订单列表')


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


def icbc(request):
    if request.method == 'GET':
        return render(request, 'icbc.html')
    else:
        return HttpResponse('...')


def test(request):
    # return render(request,'test.html',{'a':123})
    return render(request, 'test.html', {'a': 'xp'})

#
# def hosts(request):
#     '''
#     主机列表
#     :param request:请求相关的所有数据
#     :return:
#     '''
#
#     # 创建三百条数据
#     # for i in range(1,303):
#     #     # models.Host.objects.bulk_create()
#     #     hostname='c%s.com' %i
#     #     port=i
#     #     models.Host.objects.create(hostname=hostname,port=port)
#     # return HttpResponse('创建成功')
#
#     # 当前页
#     current_page = int(request.GET.get('page'))
#     # 每页显示10条数据
#     per_page = 10
#
#     start = (current_page - 1) * per_page
#     end = current_page * per_page
#
#     host_list = models.Host.objects.all()[start:end]  # []限制范围
#
#     # 生成页码
#     # 数据总条数
#     all_count = models.Host.objects.all().count()
#     pager_count, b = divmod(all_count, per_page)
#     if b != 0:
#         pager_count += 1
#
#     # 配置页码范围
#     pager_page_count = 11
#     half_pager = int(pager_page_count / 2)
#
#     # 如果总页码不足
#     if pager_count < pager_page_count:
#         page_start = 1
#         page_end = pager_count
#     else:  # 数据已经超过11条 判断当前页的大小
#         if current_page <= half_pager:
#             page_start = 1
#             page_end = 11
#         else:
#             # 如果当前页码+5大于总页码  结尾按总页码
#             if current_page + 5 > pager_count:
#                 page_end = pager_count
#                 page_start = pager_count - per_page
#             else:
#                 page_start = current_page - half_pager
#                 page_end = current_page + half_pager
#
#     page_list = []
#     if current_page == 1:
#         prev = '<a href="#">上一页</a>'
#     else:
#         prev = '<a   href="/hosts.html/?page=%s">上一页</a>' % (current_page - 1)
#     page_list.append(prev)
#     # for i in range(1,pager_count+1):
#     for i in range(page_start, page_end + 1):
#         if current_page == i:
#             tp1 = '<a class="active" href="/hosts.html/?page=%s">%s</a>' % (i, i,)
#         else:
#             tp1 = '<a href="/hosts.html/?page=%s">%s</a>' % (i, i,)
#         page_list.append(tp1)
#     if current_page >= pager_count:
#         nex = '<a href="#">下一页</a>'
#     else:
#         nex = '<a   href="/hosts.html/?page=%s">下一页</a>' % (current_page + 1)
#     page_list.append(nex)
#     page_str = "".join(page_list)
#     # page_str = '''
#     #
#     #  <a href="/hosts.html/?page=2">2</a>
#     #  <a href="/hosts.html/?page=3">3</a>
#     #  <a href="/hosts.html/?page=4">4</a>
#     # '''
#     return render(request, 'hosts.html', {'host_list': host_list, 'page_str': page_str})

def hosts(request):
    current_page=int(request.GET.get('page'))
    all_count=models.Host.objects.all().count()
    # page_obj=Page(current_page,all_count,'/hosts.html')
    page_obj=Page(current_page,all_count,request.path_info)   #path_info包含当前url
    # host_list=models.Host.objects.all()[page_obj.start(),page_obj.end()] 添加property装饰器后不用再加()调用
    host_list = models.Host.objects.all()[page_obj.start:page_obj.end]
    page_str=page_obj.page_html()
    return render(request, 'hosts.html', {'host_list': host_list, 'page_str': page_str})