from django.urls import path
from . import views


urlpatterns = [
    path('product_detail', views.submit_review, name='reviews'),
]
