from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Author, Book
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer

@api_view(['GET', 'POST'])
def index(request):
    items = Book.objects.all()
    serialized_items = BookSerializer(items, many=True, context={'request': request})
    return Response(serialized_items.data)

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
