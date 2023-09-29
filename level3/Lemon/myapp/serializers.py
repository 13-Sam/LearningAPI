from rest_framework import serializers
from . models import Category, MenuItem
from decimal import Decimal
import bleach

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    stock = serializers.IntegerField(source = 'inventory')
    def validate(self, attrs):
        # attrs['name'] = bleach.clean(attrs['name'])
        if(attrs['price']<2):
            raise serializers.ValidationError('Price should not be less than 2.0')
        if(attrs['inventory']<0):
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'category', 'price', 'price_after_tax','category_id', 'stock']
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)