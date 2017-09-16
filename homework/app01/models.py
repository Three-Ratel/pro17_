from django.db import models

# Create your models here.

#用户
class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.EmailField(null=True)
    services = models.ManyToManyField('ServiceLine')
#主机
class HostInfo(models.Model):
    name = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)
    port = models.CharField(max_length=64)
    service_line = models.ForeignKey('ServiceLine')


#业务线
class ServiceLine(models.Model):
    name = models.CharField(max_length=64)













