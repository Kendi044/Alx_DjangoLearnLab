"""
URL configuration for advanced_api_project project.

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
# api/urls.py

from django.urls import path
from .views import BookListCreateView, BookDetailUpdateDeleteView

urlpatterns = [
    # /api/books/ (GET: List, POST: Create)
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    
    # /api/books/<id>/ (GET: Detail, PUT/PATCH: Update, DELETE: Destroy)
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'),
]
