from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=100)
    discription = models.CharField(max_length=500)

