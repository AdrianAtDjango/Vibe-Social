from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('register/', views.register_view, name='register_page'),
    path('newpost/', views.new_post, name='newpost'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]