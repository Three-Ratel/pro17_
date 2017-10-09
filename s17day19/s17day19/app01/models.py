from django.db import models

# Create your models here.

class UserInof(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    email=models.EmailField(null=True)

class Host(models.Model):
    hostname=models.CharField(max_length=32)
    port=models.CharField(max_length=10)

