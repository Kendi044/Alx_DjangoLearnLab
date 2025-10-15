# blog/urls.py

from django.urls import path
from . import views
# blog/urls.py
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views # To include the register/profile views from Task 1

urlpatterns = [
    # READ: List all posts (Home page)
    path('', PostListView.as_view(), name='blog-home'),

    # CREATE: New post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    # READ: Single post detail. Use <pk> for Primary Key
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # UPDATE: Edit existing post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    
    # DELETE: Delete existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
]
