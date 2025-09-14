from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register
from .views import list_books
from .views import book_list, LibraryDetailView

urlpatterns = [
    # URL for the function-based view
    path('books/', book_list, name='book-list'),
    
    # URL for the class-based view with a dynamic primary key
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
