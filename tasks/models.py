from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    title = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.IN_PROGRESS,
        verbose_name="Статус",
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
        verbose_name="Призначений користувач",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
