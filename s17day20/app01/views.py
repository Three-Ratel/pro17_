from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.
class LoginView(View):
    #执行父类的dispatch方法   父类的dispatch通过反射找get或post
    def dispatch(self, request, *args, **kwargs):
        print('before')
        response=super(LoginView,self).dispatch(request, *args, **kwargs)
        print('after')
        return response
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

    def post(self,request,*args,**kwargs):
        print('POST')
        return HttpResponse('OK')