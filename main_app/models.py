from django.db import models
from django.urls import reverse

class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

def __str__(self):
    return self.name

# Create your models here.
