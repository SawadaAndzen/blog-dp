from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_home, name='home'),
    path('posts/', views.read_posts, name='post_list'),
    path('authors/', views.read_authors, name='author_list'),
    path('post/<int:post_id>', views.read_post, name='post'),
    path('author/<int:author_id>', views.read_author, name='author'),
]
