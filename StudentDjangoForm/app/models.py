from django.db import models

# Create your models here.

class School(models.Model):
    Scid=models.CharField(max_length=50,primary_key=True)
    Sname=models.CharField(max_length=200)

class Student(models.Model):
    Scid=models.ForeignKey(School,on_delete=models.CASCADE)
    Stid=models.CharField(primary_key=True,max_length=50)
    Stname=models.CharField(max_length=200)
    loc=models.CharField(max_length=50)
    Mobile=models.PositiveIntegerField()
    email=models.EmailField()