# api/views.py
from django_filters import rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Handles listing all books, incorporating Filtering, Searching, and Ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    # Task 2: Filtering, Searching, Ordering (Classes must be imported)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'id']
    ordering = ['title'] 


# --- Book Detail View (GET by ID) ---
class BookDetailView(generics.RetrieveAPIView):
    """
    Handles retrieving a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# --- Book Create View (POST) ---
class BookCreateView(generics.CreateAPIView):
    """
    Handles creating a new book. Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# --- Book Update View (PUT/PATCH) ---
class BookUpdateView(generics.UpdateAPIView):
    """
    Handles updating an existing book. Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# --- Book Delete View (DELETE) ---
class BookDeleteView(generics.DestroyAPIView):
    """
    Handles deleting a book. Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
