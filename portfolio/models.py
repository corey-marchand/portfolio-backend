from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    company = models.TextField(max_length=150)
    messsage = models.TextField(max_length=400)

    def __str__(self):
        return self.name