from django.urls import path, include
from .views import ListProductView

urlpatterns = [
    path('product/', ListProductView.as_view(), name='product-all')
]
