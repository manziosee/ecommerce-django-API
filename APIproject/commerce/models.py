from django.db import models
import uuid
# Create your models here.
from django.forms import ImageField

class Category(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Book(models.Model):
    title=models.CharField(max_length=200, null=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100)
    isbn=models.UUIDField(default=uuid.uuid4, primary_key=True)
    pages=models.IntegerField()
    price=models.IntegerField(default=0.0)
    stock=models.IntegerField(default=0.0)
    description=models.TextField()
    Imageurl=models.URLField()
    status=models.BooleanField()
    date_created=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    product_tag=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100)
    price=models.IntegerField(default=0.0)
    quantity=models.IntegerField(default=0.0)
    description=models.TextField()
    stock=models.IntegerField(default=0)
    ImageURL=models.URLField()
    status=models.BooleanField()
    date_created=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} , {self.product_tag}"
class Cart(models.Model):
    product=models.ManyToManyField(Product, max_length=100, blank=True)  
    books=models.ManyToManyField(Book, max_length=100, blank=True)  
    totalPrice=models.CharField(max_length=50)   