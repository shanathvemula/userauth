from __future__ import unicode_literals
from django.db import models
class Reg(models.Model):
    user = models.CharField(primary_key=True,max_length=20)
    pwd = models.CharField(max_length=20)
    email = models.EmailField()

class score(models.Model):
    user = models.ForeignKey(Reg,on_delete=models.CASCADE)
    first_round = models.IntegerField(min(0),max(10))
    second_round = models.IntegerField(min(0), max(10))
    third_round = models.IntegerField(min(0), max(10))
