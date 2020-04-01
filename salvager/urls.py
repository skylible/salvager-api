from django.urls import path, include
from .views import ListProductView
from .views import ListProductImageView
from .views import ProductDetailView
from .views import ListFaqView

urlpatterns = [
    path('products/', ListProductView.as_view(), name='product-all'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product-images/', ListProductImageView.as_view(), name='product-images-all'),
    path('faqs/', ListFaqView.as_view(), name='faq-all'),
]
