from django.contrib import admin
from .models import Product, Instagram, ProductImage, Review

# Register your models here.
admin.site.register(Product)
admin.site.register(Instagram)
admin.site.register(ProductImage)
admin.site.register(Review)
