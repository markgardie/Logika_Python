from django.urls import path
from . import views

urlpatterns = [
    # Головна сторінка з усіма постами
    path('', views.post_list, name='post-list'),
    
    # ВАЖЛИВО: Специфічні шляхи ПЕРЕД загальними
    path('post/new/', views.post_create, name='post-create'),  # ← ПЕРЕМІСТИТИ ВГОРУ
    
    # Сторінка з деталями поста (загальний паттерн)
    path('post/<slug:slug>/', views.post_detail, name='post-detail'),
    
    # Сторінка редагування поста
    path('post/<slug:slug>/edit/', views.post_edit, name='post-edit'),
    
    # Список всіх авторів
    path('authors/', views.author_list, name='author-list'),
    
    # Сторінка з деталями про автора
    path('author/<int:pk>/', views.author_detail, name='author-detail'),
]