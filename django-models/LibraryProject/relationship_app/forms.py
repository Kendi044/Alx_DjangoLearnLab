from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """
    A custom user creation form based on Django's built-in UserCreationForm.
    This form is used to handle user registration.
    """
    class Meta(UserCreationForm.Meta):
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields + ('email',)