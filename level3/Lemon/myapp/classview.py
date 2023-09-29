from rest_framework.response import Response
from . models import Category, MenuItem
from . serializers import CategorySerializer, MenuItemSerializer
from rest_framework import viewsets, generics


class MenuItemView(viewsets.ModelViewSet, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields=['price','inventory']
    search_fields=['name','category__title']
    
class CreateView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SinngleView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    

    

