from django.shortcuts import render
from rest_framework import serializers
from .models import *
from rest_framework import generics
from .serializers import *
# Create your views here.

class ListCategory(generics.ListCreateAPIView):
    queryset= Category.objects.all()
    serializer_class=Categoryserializers
 
class DetailsCategory(generics.RetrieveUpdateDestroyAPIView):
     queryset= Category.objects.all()
     serializer_class= Categoryserializers

class ListBook(generics.ListCreateAPIView):  
      queryset= Book.objects.all()
      serializer_class= Bookserializers
 
class DetailsBook(generics.RetrieveUpdateDestroyAPIView):
     queryset= Book.objects.all()
     serializer_class= Bookserializers 
     
class ListProduct(generics.ListCreateAPIView):  
      queryset= Product.objects.all()
      serializer_class= Productserializers
 
class DetailsProduct(generics.RetrieveUpdateDestroyAPIView):
     queryset= Product.objects.all()
     serializer_class= Productserializers

class ListCart(generics.ListCreateAPIView):  
      queryset= Cart.objects.all()
      serializer_class= Cartserializers
 
class DetailsCart(generics.RetrieveUpdateDestroyAPIView):
     queryset= Cart.objects.all()
     serializer_class= Cartserializers                    