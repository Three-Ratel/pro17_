from django.shortcuts import render, redirect
# from book import models
from book.models import *


# Create your views here.
def index(request):
    all_book_list = Book.objects.all()  # 取到的内容为[obj1,obj2,obj3]

    return render(request, "index.html", {"all_book_list":all_book_list})


def addBook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        author = request.POST.get('author')
        publish = request.POST.get('publish')
        print(request.POST)
        # 数据库添加操作
        Book.objects.create(title=title, price=price, author=author, publish=publish)
        return redirect("/index/")

    return render(request, "addBook.html")
def delete(request,):
    id=request.GET.get("id")
    Book.objects.filter(id=id).delete()
    return redirect("/index/")
def edit(request):
    Book.objects.filter(id=id).update(title="title")
    # Book.objects.filter()
    return redirect("/index/")