from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                messages.error(request, 'Email ou senha inválidos.')
    else:
        form = LoginForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)

def home_page(request):
    return render(request, 'home.html')