# accounts/models.py (Updated for ImageField)
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # ... other fields
    # Additional fields
    bio = models.TextField(max_length=500, blank=True)
    # 🔑 Using URLField (as per original instructions)
    profile_picture = models.URLField(max_length=200, blank=True) 
    # ManyToMany for following (Task 2)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )
    bio = models.TextField(max_length=500, blank=True)
    # 🔑 Using ImageField (Requires Pillow and Media setup)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True) 
    # ... other fields
    
    def __str__(self):
        return self.username
