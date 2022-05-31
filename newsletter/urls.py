from django.urls import path
from . import views

urlpatterns = [
    path('', views.footer_letter, name='letter-footer'),
    path('send_letters/', views.send_letter, name='send-letter')
]