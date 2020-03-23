from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ListProductView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer