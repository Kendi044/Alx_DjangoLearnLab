from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Add a success message
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') # Redirect to the login URL name
    else:
        form = UserRegistrationForm()
        
    return render(request, 'blog/register.html', {'form': form, 'title': 'Register'})

# Profile Management View
@login_required # Ensures only logged-in users can access this page
def profile(request):
    # This view can be simple initially, just displaying user info
    # For updating the profile, you'd add UserUpdateForm/ProfileUpdateForm logic here.
    return render(request, 'blog/profile.html', {'title': 'Profile'})
