from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_pic = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'email',
            'password1',
            'password2',
            'profile_pic',
        ]

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', 
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}), label='Senha')

class CreatePostForm(forms.ModelForm):
    content = forms.CharField(
            widget=forms.Textarea(
                attrs={'placeholder': 'Vamos mudar o mundo?'}
            )
        )
    
    class Meta:
        model = Post
        fields = ['content', 'image']