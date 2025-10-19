from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, CommentForm, Comment
from django.urls import reverse_lazy, reverse # Used for redirects in CBVs
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
# blog/views.py (Replace add_comment_to_post)
# blog/views.py
from django.views.generic import ListView
from django.db.models import Q  # Import Q object for complex lookups
from .models import Post
# from taggit.models import Tag, get_object_or_404 # Also ensure these are imported for tag filtering

class PostListView(ListView):
    # ... existing settings ...
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    # 🌟 Implement the search logic here
    def get_queryset(self):
        # Start with the default queryset (all posts)
        queryset = super().get_queryset()
        
        # Get the search query 'q' from the URL parameters
        query = self.request.GET.get('q') 
        
        if query:
            # Use the Q object to build a complex, multi-field search query
            queryset = queryset.filter(
                Q(title__icontains=query) |        # Search by title (case-insensitive)
                Q(content__icontains=query) |      # Search by content (case-insensitive)
                Q(tags__name__icontains=query)     # Search by tag name (case-insensitive)
            ).distinct() # Use .distinct() to avoid returning duplicate posts if they match multiple criteria (e.g., matching two different tags)
            
        return queryset

# Note: Also ensure your separate view for filtering by a specific tag is present.

# def post_list_by_tag(request, tag_slug):
#     # ... implementation for viewing posts by a specific tag

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html' # We reuse the post detail template for the form

    def form_valid(self, form):
        # 1. Fetch the parent Post object from the URL parameter
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        
        # 2. Assign the Foreign Key fields before saving
        form.instance.post = post
        form.instance.author = self.request.user
        
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the Post detail page
        return reverse('post-detail', kwargs={'pk': self.kwargs.get('pk')})

class CommentAuthorRequiredMixin(UserPassesTestMixin):
    """
    Mixin to check if the current user is the author of the comment.
    """
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        # Redirect back to the post detail page after success
        comment = self.get_object()
        return reverse('post-detail', kwargs={'pk': comment.post.pk})

class CommentUpdateView(LoginRequiredMixin, CommentAuthorRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

class CommentDeleteView(LoginRequiredMixin, CommentAuthorRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    # success_url is handled by the CommentAuthorRequiredMixin's get_success_url

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post        # Link the comment to the specific post
            comment.author = request.user # Link the comment to the logged-in user
            comment.save()
            # Redirect back to the post detail page
            return redirect('post-detail', pk=post.pk)
    
    # If not a POST request, just redirect back (or handle form errors if needed)
    return redirect('post-detail', pk=post.pk)

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

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the CommentForm to the context
        context['form'] = CommentForm() 
        return context
