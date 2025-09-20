from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, Book

# Forms for the custom user model
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo',)

# Form for the Book model
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date',)
