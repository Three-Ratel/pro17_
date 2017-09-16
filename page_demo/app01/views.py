from django.shortcuts import render, HttpResponse
from app01.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    # 批量导入
    # Booklist=[]
    # for i in range(100):
    #     Booklist.append(Book(title='book'+str(i),price=30+i*i))
    # Book.objects.bulk_create(Booklist)
    try:
        book_list = Book.objects.all()
        p = Paginator(book_list, 10)
        page = request.GET.get("page")
        book_list = p.page(page)
    except PageNotAnInteger:

        book_list = p.page(1)
    except EmptyPage:

        book_list = p.page(p.num_pages)
    return render(request, "index.html", locals())
