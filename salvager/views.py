from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .models import Product, ProductImage, Faq, Diary
from .serializers import ProductSerializer
from .serializers import ProductImageSerializer
from .serializers import FaqSerializer
from .serializers import DiarySerializer


class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveDestroyAPIView):
    """
    GET products/:id/
    PUT products/:id/
    DELETE products/:id/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs['pk'])
            return Response(ProductSerializer(a_product).data)
        except:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs['pk'])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class ListProductImageView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ListFaqView(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class ListDiaryView(generics.ListAPIView):
    queryset = Diary.objects.all()
    serializer_class = ProductImageSerializer