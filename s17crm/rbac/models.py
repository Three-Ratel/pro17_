from django.db import models

# Create your models here.
class Group(models.Model):
    title=models.CharField(max_length=32)

class Permission(models.Model):
    '''权限表'''
    title = models.CharField(verbose_name="标题", max_length=32)
    url=models.CharField(verbose_name="正则 url",max_length=256)
    code=models.CharField(verbose_name='权限代号',max_length=16)
    group=models.ForeignKey(verbose_name="权限分组",to="Group")
    is_menu=models.BooleanField(verbose_name="是否是菜单")

class UserInfo(models.Model):
    '''用户表'''
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    roles=models.ManyToManyField(to="Role")
class Role(models.Model):
    '''角色表'''
    title=models.CharField(max_length=32)
    permissions = models.ManyToManyField(to=Permission)

