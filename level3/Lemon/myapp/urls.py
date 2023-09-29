from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuItems),
    path('<int:pk>', views.single_view, name='single_view'),
]