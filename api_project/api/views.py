from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView

# The previous view for listing all books (retained for the specific 'books/' URL)
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Step 1: Create the ModelViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that automatically provides 'list', 'create', 'retrieve', 'update', 
    and 'destroy' actions for the Book model.
    """
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    
    # Step 3 (Auth): Define Permission Classes
    # Allows anyone (unauthenticated users) to read (GET, HEAD, OPTIONS).
    # Requires authentication (via token or session) for write operations 
    # (POST, PUT, PATCH, DELETE).
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
