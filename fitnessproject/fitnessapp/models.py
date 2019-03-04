from django.db import models

# Create your models here.


class fitnessmodel(models.Model):
    username = models.CharField(max_length=20)
    date = models.DateField(default='')
    calories = models.IntegerField(max_length=20)


