from django.db import models
from datetime import datetime, date
# Create your models here. Order models

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    event = models.CharField(max_length=150)
    address = models.CharField(max_length=150, blank = True)
    date = models.DateField(blank=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


