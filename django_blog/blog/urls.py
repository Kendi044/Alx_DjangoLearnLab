# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ... other blog paths (e.g., list, detail) ...
    
    # Custom Authentication Paths
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
]
