from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# User Registration View
class UserRegistrationView(FormView):
    """
    A view for user registration.
    - Uses Django's built-in UserCreationForm.
    - Redirects to the login page on successful registration.
    """
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
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

class LibrarianView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """
    View for a librarian.
    - Requires a logged-in user.
    - Only accessible if the user passes the test_func.
    """
    template_name = 'relationship_app/librarian_view.html'

    def test_func(self):
        # Placeholder for librarian role check.
        # You would typically check for a specific group or permission.
        return self.request.user.is_staff

class AdminView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """
    View for an admin user.
    - Requires a logged-in user.
    - Only accessible if the user is an admin (is_superuser).
    """
    template_name = 'relationship_app/admin_view.html'

    def test_func(self):
        return self.request.user.is_superuser
