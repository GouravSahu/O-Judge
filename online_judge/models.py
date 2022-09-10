from tkinter import CASCADE
from django.db import models
from datetime import datetime   
from django.utils.timezone import now 


# Create your models here.

class studentData(models.Model):
    sEmail=models.CharField(max_length=200)
    sName=models.CharField(max_length=200)
    sPassword=models.CharField(max_length=100)



class Problems(models.Model):
    Name=models.CharField(max_length=200)
    Statement=models.TextField()
    Code=models.TextField()
    Difficulty=models.CharField(max_length=100)
    

class Solutions(models.Model):
    Name1=models.ForeignKey(Problems, on_delete=models.CASCADE)
    Verdict=models.CharField(max_length=100)

class Testcase(models.Model):
    Name2=models.ForeignKey(Problems, on_delete=models.CASCADE)
    Input=models.TextField()
    Output=models.TextField()


'''
class mytestfiles(models.Model):
    Name2=models.ForeignKey(Problems, on_delete=models.CASCADE)
    Ifile=models.FileField(upload_to='uploads/')
    Ofile=models.FileField(upload_to='uploads/')
'''