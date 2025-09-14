from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import UserRegisterForm

class CustomLoginView(LoginView):
    """
    A custom login view to handle user authentication.
    It uses the built-in LoginView for simplicity and security.
    """
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    """
    A custom logout view that handles user session termination.
    It uses the built-in LogoutView.
    """
    template_name = 'relationship_app/logout.html'

def register(request):
    """
    A view to handle new user registration.
    It processes form data and creates a new user account.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'relationship_app/register.html', {'form': form})
