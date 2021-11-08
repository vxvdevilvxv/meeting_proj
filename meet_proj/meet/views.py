from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, 'meet/index.html')


def create_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Успешная регистрация')
            return redirect('profile')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'meet/register.html', {'form': form})


def profile_page_view(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Успешное обновление профиля')
        else:
            messages.success(request, 'Ошибка обновления профиля')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'meet/profile.html', {'profile_form': profile_form})


def login_user(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Успешная авторизация, {form.cleaned_data["username"]}')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserAuthenticationForm()
    return render(request, 'meet/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')

# Create your views here.
