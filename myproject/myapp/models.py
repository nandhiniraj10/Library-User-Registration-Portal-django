from django.db import models

# Create your models here.

class My(models.Model):
    name=models.CharField(max_length=100)
    contact_no=models.IntegerField()
    address=models.CharField(max_length=100)
    books=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    noofbook=models.CharField(max_length=100, default='')



