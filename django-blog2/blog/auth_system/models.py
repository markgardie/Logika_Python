
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    birth_date = models.DateField()
    phone = models.CharField()
    city = models.CharField()
    avatar = models.ImageField()
    bio = models.TextField()
    created_at = models.DateField()
    update_at = models.DateField()