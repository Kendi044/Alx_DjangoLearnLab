from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    """
    A custom user creation form based on Django's built-in UserCreationForm.
    This form is used to handle user registration for our CustomUser model.
    """
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'date_of_birth', 'profile_photo')

class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating a custom user.
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')
