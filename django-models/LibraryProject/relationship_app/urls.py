from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    # Your registration logic here
    pass
