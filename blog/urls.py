from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_posts, name='post_list'),
]
