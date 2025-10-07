# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# --- Book Views ---

class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles LIST (all books) and CREATE (new book) operations.
    Implements Filtering, Searching, and Ordering capabilities.
    
    Permissions: Read-only access for all, write access for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Step 4: Permissions

    # Step 1: Set Up Filtering (using DjangoFilterBackend)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Filtering fields: allows queries like ?title=Moby%20Dick
    filterset_fields = ['title', 'publication_year', 'author'] # Filter by FK 'author' ID
    
    # Step 2: Implement Search Functionality
    # Search fields: allows text search across these fields via ?search=query
    search_fields = ['title', 'author__name'] # Search in book title and nested author name
    
    # Step 3: Configure Ordering
    # Ordering fields: allows sorting via ?ordering=-publication_year
    ordering_fields = ['title', 'publication_year', 'id']
    ordering = ['title'] # Default ordering

    # Customization Instruction: Handle form submission validation (handled by DRF/Serializer)
    # The serializer's `validate_publication_year` function handles the specific validation.
    
class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles RETRIEVE, UPDATE, and DELETE operations for a single book.
    
    Permissions: Read-only access for all, write/delete access for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Step 4: Permissions
