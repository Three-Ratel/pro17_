from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)
    authors=models.ManyToManyField("Author")      #多对多如果表在下方则需要加引号
    publisher = models.ForeignKey(Publisher)    #django存储的是django_id    一对多

    #返回对象的属性
    def __str__(self):
        return self.title

#多对多表添加:
class Author(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name