from django.contrib import admin
from app.models import Post
from app.models import Author

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)