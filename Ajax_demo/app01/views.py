from django.shortcuts import render, HttpResponse
import time, json


# Create your views here.

def index(request):
    # time.sleep(2)
    return render(request, "index.html")


def sendAjax(request):
    # d={'name':"Yuan"}
    # return HttpResponse(json.dumps(d))

    username = request.POST.get("username")
    password = request.POST.get("password")
    dic = {"flag": False}
    if username == "Yuan" and password == "1234":
        dic = {"flag": True}
    return HttpResponse(json.dumps(dic))

def validate(request):
    user=request.POST.get("user")
    dic={'flag':False}
    if [12231,]:
        dic={'flag':True}

    return HttpResponse(json.dumps(dic))
