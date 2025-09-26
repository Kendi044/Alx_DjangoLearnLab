"""
URL configuration for api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from .views import BookList # Import the view you just created

urlpatterns = [
    path('admin/', admin.site.urls),
    # Maps the endpoint 'api/books/' (when included in the project) to the BookList view
    path('books/', BookList.as_view(), name='book-list'), 
    path('api/', include('api.urls')),
=======
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This line includes the API application's URL patterns under the 'api/' prefix.
    path('api/', include('api.urls')), 
>>>>>>> fbecad74eabd3ae59a44bd7d09df2922f09487c3
]
