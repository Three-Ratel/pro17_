from django.db import models

# Create your models here.

class news(models.Model):
    title=models.CharField(max_length=32)
    introduction=models.CharField(max_length=256)
    like = models.ManyToManyField(max_length=32)
    comment = models.CharField(max_length=32)
    image = models.CharField(max_length=32)
    type=models.ManyToManyField('type')
    user=models.ForeignKey('user')

class type(models.Model):
    content=models.CharField(max_length=32)


class user(models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
