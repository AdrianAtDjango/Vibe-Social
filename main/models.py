from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    nome = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return f'@{self.username}'

class Post(models.Model):
    content = models.TextField(max_length=280)
    image = models.ImageField(null=True, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.posted_by} posted {self.content} on {self.time}'