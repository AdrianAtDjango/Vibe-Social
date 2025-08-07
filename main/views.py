from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

def register_view(request):
    if request.method == 'POST':
        formlogin = LoginForm(request.POST)
        if formlogin.is_valid():
            email = formlogin.cleaned_data['email']
            password = formlogin.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                messages.error(request, 'Email ou senha inválidos.')
    else:
        formlogin = LoginForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = RegisterForm()

    context = {'form': form, 'formlogin': formlogin}
    return render(request, 'register.html', context)


@login_required
def new_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.save()            
            return redirect('home_page')
        else:
            messages.error(request, 'Algo de errado em seu post')
    else:
        form = CreatePostForm()
    
    context = {'form': form}
    return render(request, 'newpost.html', context)

@login_required
def home_page(request):
    posts = Post.objects.all().order_by('-time')
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.save()            
            return redirect('home_page')
        else:
            messages.error(request, 'Algo de errado em seu post')
    else:
        form = CreatePostForm()
    
    context = {'form': form, 'posts': posts}
    return render(request, 'list.html', context)