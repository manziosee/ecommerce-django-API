from .models import Category, Book, Product, Cart
from rest_framework import serializers

class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= '__all__'
class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields= '__all__'        
        
class Productserializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= '__all__'

class Cartserializers(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields= '__all__'        