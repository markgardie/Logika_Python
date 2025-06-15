from django import forms
from .models import Post, Author


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "content", "featured_image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "featured_image": forms.FileInput(attrs={"class": "form-control-file"}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['bio', 'profile_pic', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control-file'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }