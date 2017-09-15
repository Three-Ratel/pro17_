from django.db import models


# Create your models here.
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=6,decimal_places=2,)
    #外键建在一对多的多的表中(建在子表中)
    publisher=models.ForeignKey("Publish")
    authors=models.ManyToManyField("Author") #创建第三张表
    def __str__(self):
        return self.title
class Publish(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=32)

# class Book2Author(models.Model):
#     book=models.ForeignKey("Book")
#     author=models.ForeignKey("Author")


