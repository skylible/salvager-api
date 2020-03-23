from rest_framework import generics
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer


class ListProductView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListProductImageView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
