from django.contrib import admin
from django.urls import path, include
from .views import BookList # Import the view you just created

urlpatterns = [
    path('admin/', admin.site.urls),
    # Maps the endpoint 'api/books/' (when included in the project) to the BookList view
    path('books/', BookList.as_view(), name='book-list'), 
    path('api/', include('api.urls')),
]
