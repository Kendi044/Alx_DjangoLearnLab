# accounts/models.py (Updated for ImageField)
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # ... other fields
    bio = models.TextField(max_length=500, blank=True)
    # 🔑 Using ImageField (Requires Pillow and Media setup)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True) 
    # ... other fields
    
    def __str__(self):
        return self.username
