# blog/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Post, Comment
# Assuming 'custom_tagging_package' provides a specialized widget
from custom_tagging_package.widgets import TagWidget 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        
        # Using the widgets attribute to apply the custom widget to the 'tags' field
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Enter tags separated by commas'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Only need the content field from the user. 
        # Post and Author will be set automatically in the view.
        fields = ['content']

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
