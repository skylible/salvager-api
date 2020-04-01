from django.db import models
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.validators import MaxValueValidator, MinValueValidator
from urllib.request import urlopen

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=3000, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)

    def __str__(self):
        return self.name

class Instagram(models.Model):
    description = models.CharField(max_length=3000)
    post_url = models.URLField()
    image = models.ImageField(upload_to='instagram_images')

    def __str__(self):
        return self.description

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_images')

    def save_image_from_url(self, image_url):
        img_temp = NamedTemporaryFile(delete = True)
        img_temp.write(urlopen(image_url).read())
        img_temp.flush()

        self.image.save("image.jpg", File(img_temp), save=True)

    def __str__(self):
        return self.image.url

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews')
    headline = models.TextField(max_length=1000)
    content = models.TextField(max_length=3000)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    username = models.CharField(max_length=100)
    pub_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline

class Faq(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=3000)

    def __str__(self):
        return self.question
