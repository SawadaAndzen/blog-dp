from django.shortcuts import render
from .models import Post, Author


def read_home(request):
    
    return render(request, "home.html")


def read_posts(request):
    posts = Post.objects.all()
    
    return render(request, "post_list.html", {'posts': posts})


def read_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    return render(request, "post.html", {'post': post})


def read_authors(request):
    authors = Author.objects.all()
    
    return render(request, "author_list.html", {'authors': authors})


def read_author(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)
    
    return render(request, "author.html", {'author': author, 'posts': posts})