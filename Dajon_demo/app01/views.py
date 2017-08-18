from django.shortcuts import render, HttpResponse
# Create your views here.

import datetime


def index(request):
    timer = datetime.datetime.now()
    return HttpResponse(timer)


def login_in(request):
    if request.method == "POST":
        # print("=====>", request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        if username == "yuan" and password == "123":
            return HttpResponse("登陆成功")
        return render(request, "lgoin_in.html")


def year(request, year):
    return HttpResponse(year)


def month(request, year, month):
    return HttpResponse("year: %s month:%s" % (year, month))
