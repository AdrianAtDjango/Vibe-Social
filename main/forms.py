from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post

class RegisterForm(UserCreationForm):
    nome = forms.CharField(max_length=64, required=True)
    email = forms.EmailField(required=True)
    profile_pic = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = [
            'username',
            'nome',
            'email',
            'password1',
            'password2',
            'profile_pic',
        ]

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
