from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models
from taggit.managers import TaggableManager
# ... other imports

class Post(models.Model):
    # ... existing fields (title, content, author, created_at, etc.)
    tags = TaggableManager() # Adds the tagging field
    # ...

    def __str__(self):
        return self.title
    
    # ...

User = get_user_model() # Best practice for referencing the User model

class Comment(models.Model):
    # Link to the specific Post being commented on
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    
    # Link to the User who wrote the comment
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The actual comment content
    content = models.TextField()
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # Order comments by creation time, newest first
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title[:20]}'


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
