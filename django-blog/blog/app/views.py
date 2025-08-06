
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            author, created = Author.objects.get_or_create(user=request.user)
            post.author = author
            post.created_date = timezone.now()
            
            if 'publish' in request.POST:
                post.publish()
                messages.success(request, '🎉 Пост успішно створено та опубліковано!')
            else: 
                post.is_published = False
                post.published_date = None
                messages.success(request, '📝 Пост збережено як чернетку.')
            
            post.save()
            return redirect('post-detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'app/post_form.html', {'form': form})


@login_required
def post_edit(request, slug):
    """Редагування існуючого поста"""
    post = get_object_or_404(Post, slug=slug)
    
    if post.author.user != request.user:
        messages.error(request, '❌ Ви можете редагувати тільки свої пости.')
        return redirect('post-detail', slug=post.slug)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            
            if 'publish' in request.POST and not post.is_published:
                post.publish()
                messages.success(request, '🎉 Пост успішно опубліковано!')
            elif 'unpublish' in request.POST and post.is_published:
                post.is_published = False
                post.published_date = None
                messages.success(request, '📝 Пост знято з публікації і збережено як чернетку.')
            else:  # 'save' або будь-яка інша кнопка
                if post.is_published:
                    messages.success(request, '✅ Зміни в пості успішно збережено!')
                else:
                    messages.success(request, '📝 Чернетка поста оновлена.')
            
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