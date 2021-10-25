from django.db import models

# Create your models here.
class Problems(models.Model):
    Name=models.CharField(max_length=200)
    Statement=models.CharField(max_length=2000)
    Code=models.CharField(max_length=4000)
    Difficulty=models.CharField(max_length=100)
    

class Solutions(models.Model):
    Name1=models.ForeignKey(Problems, on_delete=models.CASCADE)
    Verdict=models.CharField(max_length=100)
    Submitted=models.DateTimeField('date published')


class Testcase(models.Model):
    Name2=models.ForeignKey(Problems, on_delete=models.CASCADE)
    Input=models.CharField(max_length=200)
    Output=models.CharField(max_length=200)


'''
class mytestfiles(models.Model):
    Name2=models.ForeignKey(Problems, on_delete=models.CASCADE)
    Ifile=models.FileField(upload_to='uploads/')
    Ofile=models.FileField(upload_to='uploads/')
'''