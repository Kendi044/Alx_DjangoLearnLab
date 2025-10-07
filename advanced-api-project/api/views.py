# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# --- Book List View (GET) ---
class BookListView(generics.ListAPIView):
    """
    Step 1: A ListView for retrieving all books.
    Includes Filtering, Searching, and Ordering functionality (Tasks 2).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    # Task 2: Filtering, Searching, Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'id']
    ordering = ['title'] 


# --- Book Detail View (GET by ID) ---
class BookDetailView(generics.RetrieveAPIView):
    """
    Step 1: A DetailView for retrieving a single book by ID.
    Read-only access for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# --- Book Create View (POST) ---
class BookCreateView(generics.CreateAPIView):
    """
    Step 1: A CreateView for adding a new book.
    Restricted to authenticated users (IsAuthenticated).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Step 4: Restrict creation to authenticated users only
    permission_classes = [IsAuthenticated]


# --- Book Update View (PUT/PATCH) ---
class BookUpdateView(generics.UpdateAPIView):
    """
    Step 1: An UpdateView for modifying an existing book.
    Restricted to authenticated users (IsAuthenticated).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Step 4: Restrict updates to authenticated users only
    permission_classes = [IsAuthenticated]


# --- Book Delete View (DELETE) ---
class BookDeleteView(generics.DestroyAPIView):
    """
    Step 1: A DeleteView for removing a book.
    Restricted to authenticated users (IsAuthenticated).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Step 4: Restrict deletion to authenticated users only
    permission_classes = [IsAuthenticated]
