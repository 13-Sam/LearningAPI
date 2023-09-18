from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books),
    path('display_even_number', views.display_even_number),
]