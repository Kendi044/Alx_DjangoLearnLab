<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token 
from .views import BookList, BookViewSet

# Step 2 (CRUD): Configure the Router
router = DefaultRouter()

# Register the ViewSet. This generates all 5 CRUD routes under the 'books_all/' prefix:
# /books_all/ (GET, POST), /books_all/<pk>/ (GET, PUT, DELETE)
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (retained from the previous task)
    path('books/', BookList.as_view(), name='book-list'),

    # Step 2 (Auth): Token Retrieval Endpoint
    # Users POST to this URL with username/password to get a token.
    path('auth/token/', obtain_auth_token, name='obtain-token'), 
    
    # Include the router URLs for BookViewSet (all CRUD operations)
    # This line connects all the automatically generated routes.
    path('', include(router.urls)), 
]
=======
from django.contrib import admin
from django.urls import path, include
from .views import BookList # Import the view you just created

urlpatterns = [
    path('admin/', admin.site.urls),
    # Maps the endpoint 'api/books/' (when included in the project) to the BookList view
    path('books/', BookList.as_view(), name='book-list'), 
    path('api/', include('api.urls')),
]
>>>>>>> fbecad74eabd3ae59a44bd7d09df2922f09487c3
