from django.urls import path
from . import views

urlpatterns = [
    path('', views.footer_letter, name='letter-footer'),
    path('send_letter/', views.send_letter, name='send-letter')
]