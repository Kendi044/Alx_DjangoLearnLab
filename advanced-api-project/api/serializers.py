# api/serializers.py

from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for the Book model.
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model, including custom validation.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        # 'author' is read-only here when used in a nested context, but
        # is required in the AuthorSerializer (see below).
        # We ensure it's required for POST operations, but allow it to be 
        # set by the view or context if necessary.
        
    # Custom field-level validation for publication_year
    def validate_publication_year(self, value):
        """
        Ensures the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Max year allowed: {current_year}."
            )
        return value


# Serializer for the Author model.
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model with nested Book serialization.
    The 'books' field handles the one-to-many relationship.
    """
    # Nested relationship: Uses the 'related_name' from the ForeignKey 
    # to serialize all related books. 'many=True' is crucial.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']