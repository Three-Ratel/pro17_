from django.db import models


# Create your models here.

class Book(models.Model):
    #id = models.IntegerField()
    title = models.CharField(max_length=32)  # 字符串
    price=models.IntegerField()
    author=models.CharField(max_length=32)
    publish=models.CharField(max_length=32)
