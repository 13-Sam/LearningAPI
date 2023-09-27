from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    

class Author(models.Model):
    name = models.CharField(max_length=255)
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    inventory = models.SmallIntegerField()
    
    
