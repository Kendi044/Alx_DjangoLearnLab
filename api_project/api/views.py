from rest_framework import generics
# Import the model and serializer we defined
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API View to list all existing Book records.
    
    By inheriting from ListAPIView, this class automatically
    implements the logic for handling HTTP GET requests.
    """
    
    # 1. Define the data source: retrieve all books from the database.
    queryset = Book.objects.all()
    
    # 2. Define the serializer class to convert the model data to JSON format.
    serializer_class = BookSerializer