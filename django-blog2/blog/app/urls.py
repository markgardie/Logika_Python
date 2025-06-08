from django.urls import path
from . import views

urlspatterns = [

    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/new', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit', views.post_edit, name='post_edit'),
    path('authors', views.author_list, name='author_list'),
    path('authors/<int:pk>', views.author_detail, name='authr_detail'),
]