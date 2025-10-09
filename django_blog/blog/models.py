from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Records the time of post creation automatically
    published_date = models.DateTimeField(auto_now_add=True)
    # Links post to a User. If the User is deleted, the post is deleted (CASCADE).
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        # A helpful representation in the Django Admin
        return self.title
