from django.contrib import admin
from . models import Category, Book, Author
# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
