from django.shortcuts import render,HttpResponse
from app01.models import  *
# Create your views here.

def index(request):
    #批量导入
    # Booklist=[]
    # for i in range(100):
    #     Booklist.append(Book(title='book'+str(i),price=30+i*i))
    # Book.objects.bulk_create(Booklist)

    book_list=Book.objects.all()

    return render(request,"index.html",locals())