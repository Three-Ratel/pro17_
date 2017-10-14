from django.shortcuts import render, HttpResponse, redirect, redirect
from django.views import View

# class BaseView(View):
#     def dispatch(self, request, *args, **kwargs):
#         if request.session.get("username"):
#             response = super(BaseView,self).dispatch(request, *args, **kwargs)
#             return response
#         else:
#             redirect('/login.html')

# Create your views here.
class LoginView(View):
    # 执行父类的dispatch方法   父类的dispatch通过反射找get或post
    # def dispatch(self, request, *args, **kwargs):
    #     print('before')
    #     response=super(LoginView,self).dispatch(request, *args, **kwargs)
    #     print('after')
    #     return response
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and pwd == '123':
            # sessionid=xxxxx写入客户端  ;  在数据库里存入{username:alex}
            request.session['username'] = user
            return redirect('/index.html')
        return render(request, 'login.html', {'msg': 'login faild'})

# class IndexView(BaseView):
#
#     def get(self, request, *args, **kwargs):
#         print(request.session['username'])
#         return HttpResponse(request.session['username'])

#多继承
class BaseView(object):
    def dispatch(self, request, *args, **kwargs):
        if request.session.get("username"):
            response = super(BaseView, self).dispatch(request, *args, **kwargs)
            return response
        else:
            redirect('/login.html')


class IndexView(BaseView,View):
    def get(self, request, *args, **kwargs):
        print(request.session['username'])
        return HttpResponse(request.session['username'])
class SomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(request.session['username'])