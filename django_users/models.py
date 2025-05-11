from django.db import models


class User(models.Model):

    ROLE_CHOICES = [
        ('admin', 'Адміністратор'),
        ('user', 'Користувач'),
    ]

    name = models.CharField(max_length=100, verbose_name="Ім'я")
    email = models.EmailField(unique=True, verbose_name="Електронна пошта")
    role = models.CharField(
        max_length=10,
        choice=ROLE_CHOICES,
        default='user',
        verbose_name='Користувач'
    )

    def __str__(self):
        return f"Ім'я: {self.name}, email: {self.email}"