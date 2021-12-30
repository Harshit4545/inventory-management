from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class books(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    book_name = models.CharField("bookname",null=True,max_length=100 )
    author_name = models.CharField("authorname",null=True,max_length=100) 
    time = models.DateField(blank=True, null=True)
    bookpdf = models.FileField()
    
