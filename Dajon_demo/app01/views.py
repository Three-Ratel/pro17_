from django.shortcuts import render, HttpResponse,redirect
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
            return redirect("/back")
    return render(request, "lgoin_in.html")


def year(request, year):
    return HttpResponse(year)


def month(request, year, month):
    return HttpResponse("year: %s month:%s" % (year, month))


def year_month(request, year, month):
    return HttpResponse("year: %s month:%s" % (year, month))


def sendByget(request):
    print(".....>>>", request.GET)
    return HttpResponse("ok")
def back(request):
    name='xp'
    return render(request,"back.html",locals())