# api/urls.py

from django.urls import path
from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView, 
    BookUpdateView, 
    BookDeleteView
)

urlpatterns = [
    # Task 1: List View (GET /api/books/)
    path('books/', BookListView.as_view(), name='book-list'),
    
    # Task 1: Create View (POST /api/books/create/)
    path('books/create/', BookCreateView.as_view(), name='book-create'), 

    # Task 1: Detail View (GET /api/books/<int:pk>/)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Task 1: Update View (PUT/PATCH /api/books/<int:pk>/update/)
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'), 
    
    # Task 1: Delete View (DELETE /api/books/<int:pk>/delete/)
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
