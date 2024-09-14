from django.shortcuts import render
from .models import Post

def read_posts(request):
    posts = Post.objects.all()
    
    return render(request, "post_list.html", {'posts': posts})