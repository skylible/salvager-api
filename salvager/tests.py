import requests
import os
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.core.files.base import ContentFile
from .models import Product
from .models import ProductImage
from .serializers import ProductSerializer

class BaseViewTest(APITestCase):
    client = APIClient()


class ProductTest(BaseViewTest):
    @staticmethod
    def create_product(name='', description='', rating=0.0, price=None, image_url=''):
        if (
            name != '' and
            description != '' and
            price is not None and
            image_url != ''
        ):
            Product.objects.create(
                name=name, description=description, rating=rating, price=price)

    def setUp(self):
        # add test data
        DEFAULT_IMAGE_URL = 'https://slimages.macysassets.com/is/image/MCY/products/6/optimized/8784586_fpx.tif?op_sharpen=1&wid=500&hei=613&fit=fit,1&$filtersm$'
        self.create_product('Perfume', 'This is a perfume',
                            0.0, 1000, DEFAULT_IMAGE_URL)
        self.create_product('Lazz', 'This is a lazz',
                            0.0, 1000, DEFAULT_IMAGE_URL)
        self.create_product('Brushie', 'This is a brushie',
                            0.0, 1000, DEFAULT_IMAGE_URL)

    def test_get_all_product(self):
        """
        This test ensures that all products added in setUp method
        exist when we make a GET request to the products/ endpoint
        """
        response = self.client.get(
            reverse("product-all", kwargs={'version': 'v1'})
        )
        expected = Product.objects.all()
        serialized = ProductSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_product(self):
        """
        This test ensures that a call for a single product exist
        when we make a GET request to the products/:id endpoint
        """
        response = self.client.get(
            reverse("product-detail", kwargs={'version': 'v1', 'pk': '1'})
        )
        expected = Product.objects.get(pk='1')
        serialized = ProductSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductImageTest(BaseViewTest):
    @staticmethod
    def create_product_image(product=None, filename='', image_url=''):
        if image_url != '' and product is not None and filename != '':
            product_image = ProductImage()
            product_image.product = product
            response = requests.get(image_url)
            if response.status_code == 200:
                product_image.image.save(filename, ContentFile(response.content), save=True)

    def setUp(self):
        # add test data
        DEFAULT_IMAGE_URL = 'https://slimages.macysassets.com/is/image/MCY/products/6/optimized/8784586_fpx.tif?op_sharpen=1&wid=500&hei=613&fit=fit,1&$filtersm$'
        DEFAULT_NAME = 'default_image.jpg'
        Product.objects.create(
                name='Perfume', description='A perfume', rating=0.0, price=100.0)
        self.create_product_image(Product.objects.get(name='Perfume'), DEFAULT_NAME, DEFAULT_IMAGE_URL)

    def test_get_product_image(self):
        """
        This test ensures that all product images added in setUp method
        exist when we make a GET request to the product_images/ endpoint
        """
        response = requests.get("http://127.0.0.1:8000/media/product_images/default_image.jpg")
        # expected = ProductImage.objects.all()
        # serialized = ProductImageSerializer(expected, many=True)
        # self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, 200)
        if os.path.exists("media/product_images/default_image.jpg"):
            os.remove("media/product_images/default_image.jpg")
