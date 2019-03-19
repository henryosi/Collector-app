from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

Services = (
    ('C', 'car wash'),
    ('G', 'gas'),
    ('B', 'body work'),
)

class Show (models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('show/aution date')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shows_detail', kwargs={'pk': self.id})


class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    shows = models.ManyToManyField(Show)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('detail', kwargs={'auto_id' : self.id}) 


class Servicing(models.Model):
    date = models.DateField('servicing date')
    service = models.CharField(max_length=1,
    choices=Services,
    default=Services[0][0]
    )
    #Create a auto_id FK
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for auto_id: {self.auto_id} @{self.url}"




# Create your models here.
