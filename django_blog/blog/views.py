from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from django.urls import reverse_lazy # Used for redirects in CBVs
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .forms import PostForm

# === 1. READ (List and Detail) ===

class PostListView(ListView):
    # Retrieve all objects from the Post model
    model = Post 
    # Specifies the template name: blog/post_list.html
    template_name = 'blog/post_list.html' 
    # Name the query result object in the template context: defaults to 'object_list'
    context_object_name = 'posts' 
    # Order by published date, newest first
    ordering = ['-published_date'] 

class PostDetailView(DetailView):
    # Displays a single instance of the Post model
    model = Post
    # Template name: blog/post_detail.html
    template_name = 'blog/post_detail.html'

# === 2. CREATE ===

class PostCreateView(LoginRequiredMixin, CreateView):
    # Only authenticated users can create posts (LoginRequiredMixin)
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog-home') # Redirect after creation (assuming 'blog-home' is your post list URL name)

    def form_valid(self, form):
        # Automatically set the post author to the logged-in user before saving
        form.instance.author = self.request.user
        return super().form_valid(form)

# === 3. UPDATE and DELETE Mixin (Permission Check) ===

class AuthorRequiredMixin(UserPassesTestMixin):
    """
    Mixin to check if the current user is the author of the post.
    Used for UpdateView and DeleteView.
    """
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# === 4. UPDATE ===

class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    # Only author can update (AuthorRequiredMixin)
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html' 
    # Note: By default, UpdateView redirects to the post's detail view after success.

# === 5. DELETE ===

class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    # Only author can delete (AuthorRequiredMixin)
    model = Post
    # Template name: blog/post_confirm_delete.html
    template_name = 'blog/post_confirm_delete.html' 
    # Must specify where to go after successful deletion
    success_url = reverse_lazy('blog-home')

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
