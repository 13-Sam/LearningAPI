from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . models import Category, MenuItem
from . serializers import CategorySerializer, MenuItemSerializer
from django.db.models import Q
# Create your views here.
@api_view(['GET', 'POST'])
def menuItems(request):
    if request.method == 'GET':
        items = MenuItem.objects.all()
        search = request.query_params.get('search')
        if search:
            items = items.filter(Q(name__icontains = search)|
                                 Q(category__title = search))
        serializer_items = MenuItemSerializer(items, many=True)
        return Response({'data': serializer_items.data}, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer_items = MenuItemSerializer(data=request.data)
        if serializer_items.is_valid():
            serializer_items.save()
            return Response({'data': serializer_items.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer_items.errors}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view()
def single_view(request, pk):
    item = MenuItem.objects.get(id=pk)
    serialized_item = MenuItemSerializer(item)
    return Response({'data': serialized_item.data}, 200)