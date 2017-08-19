from django.shortcuts import render, HttpResponse
import datetime


# Create your views here.
def timer(request):
    t_obj = datetime.datetime.now()
    l = [11, 2, 3, ]
    d = {"name": "egon", "age": 34}
    # return render(request, "timmer.html", {"t": t_obj})
    return render(request, "timmer.html", {"t": t_obj, "li": l, "dic": d})
