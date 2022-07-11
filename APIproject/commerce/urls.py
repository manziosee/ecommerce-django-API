from typing import List
from django.urls import path
from .views import *

urlpatterns = [
    path('listcategory',ListCategory.as_view(),name='category'),
    path('retrievecategory/<int:pk>/', DetailsCategory.as_view(), name='category'),
    path('listBook', ListBook.as_view(), name='Book'),
    path('retrieveBook/<int:pk>/', DetailsBook.as_view(), name='Book'),
    path('listproduct',ListProduct.as_view(), name='product'),
    path('retrieveproduct/<int:pk>/', DetailsProduct.as_view(), name='product'),
    path('listcart',ListCart.as_view(), name='cart'),
    path('retrievecart/<int:pk>/',DetailsCart.as_view(), name='cart')
]
