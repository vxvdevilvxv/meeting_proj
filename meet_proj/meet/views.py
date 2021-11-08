from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse
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
            return redirect('create_profile')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'meet/register.html', {'form': form})


def create_profile(request):
    profile = request.user
    print(profile)
    return HttpResponse('Hello')
    #return render(request, 'meet/create_profile.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
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
