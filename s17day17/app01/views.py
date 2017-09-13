from django.shortcuts import render,HttpResponse

# Create your views here.
from app01.models import *
def addArticle2(request):
    #方法一 直接操作库
    # Book.objects.create(id=1,title='python',publication_date='2017-03-04',price='11.15',publisher_id=1)
    #方法二 先查询再操作
    # p1=Publisher.objects.get(name='人大出版社')
    # Book.objects.create(id=3,title='python3',publication_date='2017-05-04',price=98.2,publisher=p1)
    # return HttpResponse('sucess')
#--------------------------------------------------------------------------------------
    '''多对多的添加如下'''
    # Book.objects.get(title='python3')
    book_obj=Book.objects.filter(title='python3').first()   #.first获得对象 默认是集合  或者.[0]
    # print('======>',book_obj.authors)#所有作者的集合对象
    # author_obj1=Author.objects.get(id=1)
    # author_obj2=Author.objects.get(id=2)
    # book_obj.authors.add(author_obj1,author_obj2) #将上述的结果的对应关系放到第三张表中
    #book_obj.authors.remove(author_obj1, author_obj2)   #删除

    #*号的使用
    authors_all=Author.objects.all()
    # book_obj.authors.remove(*[author_obj1,author_obj2])
    book_obj.authors.remove(*authors_all)

    return HttpResponse('sucess')


def show(request):
    book_list=Book.objects.all()

    #value的使用 结果不是对象 而是对象的某个字段或属性 结果也为querySet
    ret1=Book.objects.values('title')
    ret1_list = Book.objects.values_list('title')
    print('ret1 is : ',ret1)        #结果是:ret1 is :  <QuerySet [{'title': 'python'}, {'title': '西游记'}, {'title': 'python3'}]>
    print(ret1_list)                 #结果为querySet里的列表<QuerySet [('python',), ('西游记',), ('python3',)]>
    return render(request,'dateshow.html',locals())

def edit(request):
    # Book.objects.filter(id=2).update(title='红楼梦')         #效率更高
    b=Book.objects.filter(id=2).first()
    b.title='西游记'
    b.save()
    return HttpResponse('编辑成功')