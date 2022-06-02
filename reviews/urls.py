from django.urls import path
from . import views


urlpatterns = [
    path('product_detail', views.submit_review, name='reviews'),
    path('update_review/<pk>/', views.UpdateReview.as_view(),
         name='update_review'),
    path('delete_review/<pk>/',
         views.DeleteReview.as_view(),
         name='delete_review'),
]
