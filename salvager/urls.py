from django.urls import path, include
from .views import ListProductView, ListProductImageView

urlpatterns = [
    path('products/', ListProductView.as_view(), name='product-all'),
    path('product-images/', ListProductImageView.as_view(), name='product-images-all')
]
