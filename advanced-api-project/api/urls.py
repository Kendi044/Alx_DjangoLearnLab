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
    # Task 1: List View (GET) and Create View (POST)
    # The LIST and CREATE endpoints typically share the same base URL (books/)
    # They are separated into two distinct views here for compliance with the request.
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'), # Explicit create path

    # Task 1: Detail, Update, and Delete operate on a single resource ID (<int:pk>)
    
    # Detail View (GET)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Update View (PUT/PATCH) - Typically uses the same URL as Detail, but handles different methods
    # For separation required by the task, we'll keep the views distinct but use clean paths:
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'), 
    
    # Delete View (DELETE) - Typically uses the same URL as Detail, but handles different methods
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
