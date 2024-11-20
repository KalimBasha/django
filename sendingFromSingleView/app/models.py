from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(primary_key=True,max_length=200,null=False,blank=False)

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    url=models.URLField()
    email=models.EmailField()
    img=models.ImageField()

class AccessRecords(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    author=models.CharField(max_length=50)
    files=models.FileField()