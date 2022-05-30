from django.urls import path
from . import views

urlpatterns = [
    path('base', views.footer_letter, name='letter-footer'),
    path('send_letter/', views.mail_letter, name='send-letter')
]