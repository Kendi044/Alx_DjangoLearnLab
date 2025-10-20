# accounts/urls.py
from django.urls import path
from .views import UserRegistrationView, CustomAuthToken

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    # Add a view for profile management later if needed
]