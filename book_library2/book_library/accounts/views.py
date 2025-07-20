from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import UserProfile
from .forms import UserForm, UserProfileForm

class LoginView(BaseLoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('library:book_list')

    def form_valid(self, form):
        messages.success(self.request, 'Ви успішно увійшли')

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy('library:book_list')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Ви вийшли із системи')
        return super().dispatch(request, *args, **kwargs)