from django.shortcuts import render, HttpResponse
from app01.models import *
from django.db.models import Avg,Max,Min,Sum,F,Q

# Create your views here.
def index(request):
    return HttpResponse('首页')


def add(request):
    # 单表操作
    # create方式
    # Book.objects.create(title='python',price=233)
    # save方式
    # book_obj=Book(title='linux',price=122)
    # book_obj.save()

    # 一对多添加
    # Book.objects.create(title='python',price=23,publisher_id=2)


    # book_obj=Book.objects.get(nid=1)
    # print(book_obj.title,book_obj.price)
    # print(book_obj.publisher)  #是nid=1的这本书的关联的出版社对象(一个)

    # 一对多的添加方式二
    # publish_obj=Publish.objects.get(id=1)
    # book_obj=Book(title='linux',price=122,publisher=publish_obj)#增加外键字段 或者如下行
    # # book_obj.publisher=publish_obj
    # book_obj.save()

    # 多对多添加
    # book_obj=Book.objects.get(nid=2)
    # # author_list=Author.objects.all()
    # # book_obj.authors.add(*author_list)
    # # book_obj.authors  #nid=2的书关联的作者对象集合
    # book_obj.authors.clear()    #remove 删除单个的时候使用

    # 多对多添加方式 手动创建表 在models里面创建
    # Book2Author.objects.create(book_id=1, author_id=1)

    return HttpResponse('ok')


def query(request):
    ret = Book.objects.values(
        'title')  # 字典结果  <QuerySet [{'title': 'python'}, {'title': 'linux'}, {'title': '金瓶梅'}, {'title': '水浒传'}]>
    ret2 = Book.objects.filter(nid__gt=2).values('title', 'price')
    ret3 = Book.objects.filter(nid__gt=2).values_list('title', 'price')  # 元组 没有键
    print(ret)
    print(ret2)
    print(ret3)
    return HttpResponse('ok')


def index(request):
    # return HttpResponse('ok')
    book_list = Book.objects.all()
    print('book_list is :', book_list)
    if request.method == "POST":
        keyWord = request.POST.get("key_word")
        book_list = Book.objects.filter(title__icontains=keyWord)
    return render(request, 'index.html', locals())


# 多表查询
def relate_query(request):
    # ######通过对象的方式
    # #######一对多
    # book_obj=Book.objects.get(title='python')
    # #ret=book_obj.publisher 出版社名字
    # ret=book_obj.publisher.email  #出版社联系方式
    # print(ret)
    ####### 多对多
    # 查询Linux的所有作者名字
    # book_obj=Book.objects.get(title='linux')
    # author_list=book_obj.authors.all()
    # for author in author_list:
    #     print(author.name)

    # -------------------双下划线的方式进行查询-------------
    # 单表
    # ret=Book.objects.filter(title='python').values('price')
    # print(ret)  #<QuerySet [{'price': Decimal('23.00')}]>

    # 多表   values filter都可以跨表
    # 查询python的出版社联系方式
    # ret=Book.objects.filter(title='python').values('publisher__email')
    # print(ret)
    # 查询python这本书的所有作者的名字
    # ret=Book.objects.filter(title='python').values('authors__name')
    # print(ret)

    # 查询所有alex出版过的书籍名称
    # 方式一 正向查询 通过子表
    # ret=Book.objects.filter(authors__name='alex').values('title') #多表   values filter都可以跨表
    # print(ret)
    # 方式二 反向查询 使用'表名__字段'进行跨表
    ret = Author.objects.filter(name='alex').values('book__title')
    print(ret)

    # 正向
    ret1 = Book.objects.filter(title='python').values('publisher__name')
    # 反向
    ret2 = Publish.objects.filter(book__title='python').values('name')
    print(ret1, ret2)
    return HttpResponse('OK2')


# 聚合分组
def query2(request):

    #######聚合 aggregate
    # # 查询book表中所有书籍的平均价格
    # # select AVG(price) from book
    # ret=Book.objects.all().aggregate(Avg('price'))#    ret=Book.objects.all().aggregate(Avg('price'))#
    # ret = Book.objects.all().aggregate(priceavg=Avg('price'))#自定义键   结果为:{'priceavg': 44.75}
    # ret = Book.objects.all().aggregate(priceavg=Avg('price'),maxPrice=Max('price'))
    # print(ret)

    #分组查询
    #oldboy出过的书价格总和
    ret=Book.objects.filter(authors__name='oldboy').aggregate(Sum('price'))
    print(ret)
    #每一个作者出过的书的总价格
    priceSum=Book.objects.values('authors__name').annotate(Sum('price'))
    print(priceSum)

    return HttpResponse('OK')

def query3(request):
    #F查询
    #Book.objects.update(price=F('price')+100)

    #Q查询  与或非  &|~
    ret=Book.objects.filter(
        Q(title__istartswith='P')|Q(title__istartswith='L')
    )
    print(ret)

    return HttpResponse('OK')