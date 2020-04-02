# What is this?

This is a project of cosmetic website. This app is built with Django and functions as REST API for the main website, which is built using ReactJS.

# Environment

Python 3.7.7

Django 3.0.4

# Needed Dependencies

Pillow

djangorestframework

Requests

django-cors-headers

# What endpoints are available?

For now, there are only 3 endpoints available

GET /api/v1/products : list all products with child models

GET /api/v1/products/:id : get product based on id with its child models

GET /api/v1/product-images : list all product images available on the server

GET /api/v1/faqs : list all faqs available on the server

GET /api/v1/diaries : list all diaries available on the server


# How to get product image?

Just start with website url followed by the path provided by the api

For example: http://localhost:8000/media/product-images/perfume.png
