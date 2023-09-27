from . models import Category, Author, Book
from rest_framework import serializers
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
        
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'stock','price_after_tax', 'category', 'category_id', 'author_id']
        
    def calculate_tax(self, product:Book):
        return product.price * Decimal(1.1)

# class BookSerializer(serializers.ModelSerializer):
#     # category = CategorySerializer()
#     stock = serializers.IntegerField(source='inventory')
#     price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     category = serializers.HyperlinkedRelatedField(
#         queryset=Category.objects.all(),
#         view_name='category-detail', 
#         lookup_field = 'id',
#         # read_only = True
#     )
#     author = serializers.HyperlinkedRelatedField(
#         queryset=Author.objects.all(),
#         view_name='author-detail',  # Ensure this matches your URL pattern's name
#         lookup_field='id'
#     )
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', 'price', 'stock','price_after_tax', 'category']
        
#     def calculate_tax(self, product:Book):
#         return product.price * Decimal(1.1)
            