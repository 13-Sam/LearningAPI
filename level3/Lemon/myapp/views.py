from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from . models import Category, MenuItem
from . serializers import CategorySerializer, MenuItemSerializer
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from . throttle import TenPerMinute

# Create your views here.
@api_view(['GET', 'POST'])
def menuItems(request):
    if request.method == 'GET':
        items = MenuItem.objects.all()
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default = 2)
        page = request.query_params.get('page', default = 1)
        if search:
            items = items.filter(Q(name__icontains = search)|
                                 Q(category__title = search))
        if ordering:
            items = items.order_by(ordering)
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number = page)
        except EmptyPage:
            items = []
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

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'message': 'secret message'}, 200)

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenPerMinute])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({'message': 'message for manager'}, 200)
    else:
        return Response({'message': 'not for u'}, 400)

@api_view()
@throttle_classes([AnonRateThrottle])
def anon_throttle(request):
    return Response({'message': 'msg for anonymous'})