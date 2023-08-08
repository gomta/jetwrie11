from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    last_name = models.CharField(max_length=90,verbose_name='نام خانوادگی',null=True,blank=True)
    first_name = models.CharField(max_length=150,verbose_name='نام',null=True,blank=True)
    pictures = models.ImageField(upload_to="images/",unique=False,verbose_name='عکس برای پروفایل',null=True,blank=True)
    shterak = models.BooleanField(default=False,verbose_name="اشتراک ویژه")
