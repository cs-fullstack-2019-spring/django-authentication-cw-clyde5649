from django.db import models

# Create your models here.


#models for what i want the user to input#

class fitnessmodel(models.Model):
    username = models.CharField(max_length=20)
    date = models.DateField(default='')
    calories = models.IntegerField(default='')


