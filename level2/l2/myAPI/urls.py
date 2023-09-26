from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book/<int:id>/', views.singleView),
    path('category/<int:id>/', views.category_detail, name='category-detail'),
    path('author/<int:id>/', views.author_detail, name='author-detail'),
]
