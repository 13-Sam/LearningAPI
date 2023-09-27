from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .models import Category, Author, Book
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

@api_view(['GET', 'POST'])
# @renderer_classes([TemplateHTMLRenderer])
def index(request):
    if request.method == 'GET':
        items = Book.objects.select_related('category', 'author').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('price')
        search = request.query_params.get('search')
        if category_name:
            items = items.filter(category__title = category_name)
            
        if to_price:
            items = items.filter(price = to_price)
            
        if search:
            items = items.filter(title__icontains = search)
        serialized_items = BookSerializer(items, many=True, context={'request': request})

        return Response({'data': serialized_items.data}, status=status.HTTP_200_OK)  
    elif request.method == 'POST':
        serialized_items = BookSerializer(data=request.data)
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items.data, status=status.HTTP_201_CREATED)
    
    
    # if request.method == 'GET':
    #     items = Book.objects.all()
    #     serialized_items = BookSerializer(items, many=True, context={'request': request})
    #     return Response(serialized_items.data)
    # elif request.method == 'POST':
    #     serialized_items = BookSerializer(data=request.data)
    #     serialized_items.is_valid(raise_exception=True)
    #     serialized_items.save()
    #     return Response(serialized_items.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
def singleView(request, id):
    item = get_object_or_404(Book, pk=id)
    serialized_item = BookSerializer(item, context={'request': request})
    return Response(serialized_item.data)

@api_view(['GET'])
def category_detail(request, id):
    category = get_object_or_404(Category, pk=id)
    serialized_category = CategorySerializer(category, context={'request': request})
    return Response(serialized_category.data)

@api_view(['GET'])
def author_detail(request, id):
    author = get_object_or_404(Author, pk=id)
    serialized_author = AuthorSerializer(author, context={'request': request})
    return Response(serialized_author.data)
