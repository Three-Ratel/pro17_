from django.shortcuts import render,HttpResponse
from app01.models import *
# Create your views here.
def index(request):
    return HttpResponse('首页')

def add(request):
    #单表操作
    #create方式
    #Book.objects.create(title='python',price=233)
    #save方式
    # book_obj=Book(title='linux',price=122)
    # book_obj.save()

    #一对多添加
    # Book.objects.create(title='python',price=23,publisher_id=2)


    # book_obj=Book.objects.get(nid=1)
    # print(book_obj.title,book_obj.price)
    # print(book_obj.publisher)  #是nid=1的这本书的关联的出版社对象(一个)

    #一对多的添加方式二
    # publish_obj=Publish.objects.get(id=1)
    # book_obj=Book(title='linux',price=122,publisher=publish_obj)#增加外键字段 或者如下行
    # # book_obj.publisher=publish_obj
    # book_obj.save()

    #多对多添加
    # book_obj=Book.objects.get(nid=2)
    # # author_list=Author.objects.all()
    # # book_obj.authors.add(*author_list)
    # # book_obj.authors  #nid=2的书关联的作者对象集合
    # book_obj.authors.clear()    #remove 删除单个的时候使用

    #多对多添加方式 手动创建表 在models里面创建
    Book2Author.objects.create(book_id=1,author_id=1)


    return HttpResponse('ok')

def query(request):
    ret=Book.objects.values('title')#字典结果  <QuerySet [{'title': 'python'}, {'title': 'linux'}, {'title': '金瓶梅'}, {'title': '水浒传'}]>
    ret2 = Book.objects.filter(nid__gt=2).values('title','price')
    ret3 = Book.objects.filter(nid__gt=2).values_list('title', 'price')#元组 没有键
    print(ret)
    print(ret2)
    print(ret3)
    return HttpResponse('ok')