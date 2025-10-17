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
# blog/urls.py (Add to existing urlpatterns)

from .views import CommentUpdateView, CommentDeleteView, add_comment_to_post
from django.contrib.auth import views as auth_views
app_name = 'blog' 

urlpatterns = [
    # ... CRUD URLs from Task 2 ...

    # Comment Creation: /post/1/comment/new/
    path('post/<int:pk>/comments/new/', add_comment_to_post, name='add-comment'),
    
    # Comment Update: /comment/1/edit/ (uses comment PK)
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    
    # Comment Delete: /comment/1/delete/ (uses comment PK)
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    
    path('', PostListView.as_view(), name='blog-home'),

    # CREATE: New post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    # READ: Single post detail. Use <pk> for Primary Key
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # UPDATE: Edit existing post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    
    # DELETE: Delete existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # You might also want logout
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    # ... other paths ...
]
