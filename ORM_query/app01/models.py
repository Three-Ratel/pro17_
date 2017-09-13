from django.db import models


# Create your models here.
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=6,decimal_places=2,)
