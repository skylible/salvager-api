from django.urls import path
from .views import ListProductView
from .views import ListProductImageView
from .views import ProductDetailView
from .views import ListFaqView
from .views import ListDiaryView
from .views import ListInstagramView

urlpatterns = [
    path('products/', ListProductView.as_view(), name='product-all'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product-images/', ListProductImageView.as_view(), name='product-images-all'),
    path('faqs/', ListFaqView.as_view(), name='faq-all'),
    path('instagrams/', ListInstagramView.as_view(), name='instagram-all'),
    path('diaries/', ListDiaryView.as_view(), name='diary-all')
]
