from django.urls import path
from . import views

urlpatterns = [
    # Auth views
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    # Role-based views
    path('member/', views.MemberView.as_view(), name='member_view'),
    path('librarian/', views.LibrarianView.as_view(), name='librarian_view'),
    path('admin/', views.AdminView.as_view(), name='admin_view'),
    
    # Book-related views with permissions
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit/', views.BookEditView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
