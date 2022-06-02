from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product_detail', views.reviews, name='reviews')
]