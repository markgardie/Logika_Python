from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserUpdateForm, ProfileUpdateForm

def login_view(request):
    pass


def logout_view(request):
    pass


def signup_view(request):
    pass


@login_required
def profile_view(request):
    pass


@login_required
def profile_edit(request):
    pass

