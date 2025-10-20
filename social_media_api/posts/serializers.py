# posts/serializers.py

from rest_framework import serializers
# 🔑 IMPORTANT: Only import the models here, do NOT redefine them.
from .models import Post, Comment 

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'author_username', 'content', 'created_at')
        read_only_fields = ('author',)

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    # Use the CommentSerializer for nested comments display
    comments = CommentSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        fields = ('id', 'author', 'author_username', 'title', 'content', 'created_at', 'comments')
        read_only_fields = ('author',)

    