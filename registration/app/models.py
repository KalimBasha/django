from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)   #one to one field bcz one user has unique profile and picture
    Address=models.TextField()     #to create a textarea
    profile_pic=models.ImageField()   #to get the image and to use this field we have to install pillow module from pip by syntax pip install pillow