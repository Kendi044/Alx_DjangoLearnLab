from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Converts Book model instances to JSON format for the API.
    
    This serializer is crucial as it defines the fields that are 
    exposed through the API and handles the serialization (Model -> JSON).
    """
    class Meta:
        # Link this serializer directly to the Book model
        model = Book
        
        # Use '__all__' to automatically include the model's fields (id, title, author)
        fields = '__all__'