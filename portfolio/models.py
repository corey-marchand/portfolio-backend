from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    messsage = models.TextField(max_length=200)

    def __str__(self):
        return self.name