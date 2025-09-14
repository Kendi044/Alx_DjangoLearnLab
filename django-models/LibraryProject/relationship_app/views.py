from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator, permission_required
from .forms import UserRegisterForm, BookForm
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Function-based view to list all books
def book_list(request):
    """
    Renders a list of all books stored in the database.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Renders details for a specific library, including all books it contains.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Define a function to check if the user is a librarian
def is_librarian(user):
    return user.is_staff

# Define a function to check if the user is an admin
def is_admin(user):
    return user.is_superuser
@user_passes_test

# User Registration View
class UserRegistrationView(FormView):
    """
    A view for user registration.
    - Uses Django's built-in UserCreationForm.
    - Redirects to the login page on successful registration.
    """
    template_name = 'relationship_app/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Role-Based Views
class MemberView(LoginRequiredMixin, TemplateView):
    """
    View for a standard member.
    - Requires a logged-in user to access.
    """
    template_name = 'relationship_app/member_view.html'

@method_decorator(user_passes_test(is_librarian), name='dispatch')
class LibrarianView(LoginRequiredMixin, TemplateView):
    """
    View for a librarian.
    - Requires a logged-in user.
    - Only accessible if the user passes the test.
    """
    template_name = 'relationship_app/librarian_view.html'

@method_decorator(user_passes_test(is_admin), name='dispatch')
class AdminView(LoginRequiredMixin, TemplateView):
    """
    View for an admin user.
    - Requires a logged-in user.
    - Only accessible if the user is an admin.
    """
    template_name = 'relationship_app/admin_view.html'

@method_decorator(permission_required('relationship_app.can_add_book', raise_exception=True), name='dispatch')
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('list_books')

@method_decorator(permission_required('relationship_app.can_change_book', raise_exception=True), name='dispatch')
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('list_books')

@method_decorator(permission_required('relationship_app.can_delete_book', raise_exception=True), name='dispatch')
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('list_books')

# A view to list all books. This is not part of the secured views.
class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/book_list.html'


