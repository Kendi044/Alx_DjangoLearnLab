from django.urls import path
from .views import BookListCreateView, BookDetailUpdateDeleteView

urlpatterns = [
    # /api/books/ (GET: List, POST: Create)
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    
    # /api/books/<id>/ (GET: Detail, PUT/PATCH: Update, DELETE: Destroy)
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'),
]
