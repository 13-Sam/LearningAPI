from rest_framework import serializers
from . models import Category, MenuItem
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    stock = serializers.IntegerField(source = 'inventory')
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'category', 'price', 'price_after_tax','category_id', 'stock']
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)