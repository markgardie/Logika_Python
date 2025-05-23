from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Author
from .forms import PostForm, AuthorForm


def post_list(request):
    """Відображення списку всіх опублікованих постів"""
    posts = Post.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'app/post_list.html', {'posts': posts})


def post_detail(request, slug):
    """Відображення деталей поста"""
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'app/post_detail.html', {'post': post})


@login_required
def post_create(request):
    """Створення нового поста"""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # Отримуємо або створюємо автора на основі поточного користувача
            author, created = Author.objects.get_or_create(user=request.user)
            post.author = author
            post.created_date = timezone.now()
            post.save()
            return redirect('post-detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'app/post_form.html', {'form': form})


@login_required
def post_edit(request, slug):
    """Редагування існуючого поста"""
    post = get_object_or_404(Post, slug=slug)
    
    # Перевірка чи користувач є автором поста
    if post.author.user != request.user:
        return redirect('post-detail', slug=post.slug)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post-detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/post_form.html', {'form': form})


def author_list(request):
    """Відображення списку всіх авторів"""
    authors = Author.objects.all()
    return render(request, 'app/author_list.html', {'authors': authors})


def author_detail(request, pk):
    """Відображення деталей автора"""
    author = get_object_or_404(Author, pk=pk)
    author_posts = Post.objects.filter(author=author, is_published=True).order_by('-published_date')
    return render(request, 'app/author_detail.html', {
        'author': author,
        'posts': author_posts
    })