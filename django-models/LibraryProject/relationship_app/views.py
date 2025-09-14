from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

# This class handles the logout functionality
class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# This function-based view handles user registration
def register(request):
    """
    Handles user registration.

    This view processes both GET and POST requests for user registration.
    - If the request method is POST and the form is valid, it saves the new user
      and redirects to the login page.
    - If the request is GET, it displays an empty registration form.
    """
    # Check if the request is a POST request
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = UserCreationForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the new user
            form.save()
            # Display a success message to the user
            messages.success(request, f'Your account has been created! You are now able to log in.')
            # Redirect the user to the login page
            return redirect('login')
    else:
        # If it's a GET request, create an empty form
        form = UserCreationForm()
    
    # Render the registration page with the form
    return render(request, 'relationship_app/register.html', {'form': form})
