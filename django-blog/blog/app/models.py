from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, verbose_name="Біографія")
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True, verbose_name="Фото профілю")
    website = models.URLField(blank=True, verbose_name="Веб-сайт")
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def get_posts_count(self):
        return self.posts.count()


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', verbose_name="Автор")
    content = models.TextField(verbose_name="Зміст")
    featured_image = models.ImageField(upload_to='post_images', blank=True, null=True, verbose_name="Зображення")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата створення")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата публікації")
    is_published = models.BooleanField(default=False, verbose_name="Опубліковано")
    
    class Meta:
        ordering = ['-published_date', '-created_date']
        verbose_name = "Пост"
        verbose_name_plural = "Пости"
    
    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.slug)])