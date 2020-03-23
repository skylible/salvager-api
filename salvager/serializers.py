from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    product_images = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ("name", "description", "price", "rating", "product_images")

