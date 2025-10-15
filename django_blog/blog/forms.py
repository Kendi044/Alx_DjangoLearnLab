# blog/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # We only want the user to input the title and content.
        # The 'author' and 'published_date' will be set automatically in the view.
        fields = ['title', 'content']
User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        # Ensure 'email' is included in the fields
        fields = ('username', 'email', )