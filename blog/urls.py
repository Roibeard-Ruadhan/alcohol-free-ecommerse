from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blog'),
    path('<int:blog_post_id>/', views.blog_detail, name='blog_detail'),
    path('add_blog/', views.add_blog_post, name='add_blog'),
    path('edit_blog/<int:blog_post_id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<pk>/',
         views.Delete_Blog_Post.as_view(),
         name='delete_blog'),
    path('update_comment/<int:pk>/', views.EditCommentView.as_view(),
         name='update_comment'),
    path(
         'delete_comment/<pk>/',
         views.DeleteComment.as_view(),
         name='delete_comment'),
]
