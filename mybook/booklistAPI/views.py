from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from . models import Book
from . serializers import BookSerializer

class CreateBookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class EditBook(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
# @api_view()
# def books(request):
#     return Response('list of books', status=status.HTTP_200_OK)

# class Books(viewsets.ViewSet):
#     def list(self, request):
#         return Response({"message":"All books"}, status.HTTP_200_OK)
#     def create(self, request):
#         return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    

# class Books(APIView):
#     def get(self, request):
        # author = request.GET.get('author')
        # if(author):
        #     return Response({'message':'this is book is owned by' }+ author, status=status.HTTP_200_OK)
    #     return Response('list of books', status.HTTP_200_OK)
    
    # def post(self, request):
    #     return Response('ok', 201)
    
# class Book(APIView):
#     def get(self, request):
#         name = request.GET.get('name')
#         if(name):
#             return Response({'message': 'this book is written by '+name}, status.HTTP_200_OK)
#         return Response('get request', status.HTTP_200_OK)
#     def post(self, request):
#         return Response({'title': request.data.get('title')}, status.HTTP_201_CREATED)
