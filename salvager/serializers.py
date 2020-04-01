from rest_framework import serializers
from .models import Product, ProductImage, Review, Faq

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    product_images = serializers.StringRelatedField(many=True)
    # product_reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        depth = 1
        fields = ("name", "description", "price", "rating", "product_images", "product_reviews")

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("headline", "content", "rating", "username", "pub_time")

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ("question", "answer")
