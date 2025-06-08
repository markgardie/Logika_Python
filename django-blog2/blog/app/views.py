from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Author
from .forms import PostForm, AuthorForm 

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(is_published = True).order_by('-published_date')
    return render(request, 'app/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'app/post_detail.html', {'post': post})

def post_create():
    pass

def post_edit():
    pass

def author_list():
    pass

def author_detail():
    pass