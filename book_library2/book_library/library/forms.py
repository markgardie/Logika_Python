from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'cover', 'publication_date', 
                  'isbn', 'pages', 'genre']
        labels = {
            'title': 'Назва книги',
            'author': 'Автор',
            'description': 'Опис',
            'cover': 'Обкладинка',
            'publication_date': 'Дата публікації',
            'isbn': 'ISBN',
            'pages': 'Кількість сторінок',
            'genre': 'Жанр',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
        }
