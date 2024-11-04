from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    portfolio = models.CharField(max_length=100)
    persona = models.CharField(max_length=100)

    def __str__(self):
        return self.name
