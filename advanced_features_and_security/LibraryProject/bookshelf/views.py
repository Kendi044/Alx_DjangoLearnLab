from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import UserRegistrationForm
from .models import Book
from .forms import ExampleForm

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

@method_decorator(permission_required('relationship_app.can_view', raise_exception=True), name='dispatch')
class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            'books': books
        }
        return render(request, 'relationship_app/book_list.html', context)

@method_decorator(permission_required('relationship_app.can_create', raise_exception=True), name='dispatch')
class BookCreateView(View):
    def get(self, request):
        return render(request, 'relationship_app/book_form.html')

    def post(self, request):
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        Book.objects.create(
            title=title,
            author=author,
            publication_date=publication_date
        )
        return redirect('book_list')

@method_decorator(permission_required('relationship_app.can_edit', raise_exception=True), name='dispatch')
class BookEditView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        context = {
            'book': book
        }
        return render(request, 'relationship_app/book_form.html', context)

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_date = request.POST.get('publication_date')
        book.save()
        return redirect('book_list')

@method_decorator(permission_required('relationship_app.can_delete', raise_exception=True), name='dispatch')
class BookDeleteView(View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('book_list')

class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})

class MemberView(View):
    def get(self, request):
        return render(request, 'relationship_app/member_view.html')

class LibrarianView(View):
    def get(self, request):
        return render(request, 'relationship_app/librarian_view.html')

class AdminView(View):
    def get(self, request):
        return render(request, 'relationship_app/admin_view.html')
