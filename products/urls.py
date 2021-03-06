from django.urls import path
from . import views
from reviews.views import submit_review, UpdateReview, DeleteReview


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<pk>', views.Delete_Product.as_view(),
         name='delete_product'),
    path('submit_review/<int:product_id>/', views.submit_review,
         name='submit_review'),
    path('update_review/<pk>/', views.UpdateReview.as_view(),
         name='update_review'),
    path('delete_review/<pk>/',
         views.DeleteReview.as_view(),
         name='delete_review'),
]