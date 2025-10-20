# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Additional fields
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.URLField(max_length=200, blank=True)
    # ManyToMany for following (Task 2 will modify this)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username
