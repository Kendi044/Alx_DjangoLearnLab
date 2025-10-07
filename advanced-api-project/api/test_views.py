# api/test_views.py (Updated with self.client.login)

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Test suite for the Book CRUD endpoints, custom validation, and querying features.
    """
    def setUp(self):
        # 1. Setup API Client and Users
        self.client = APIClient()
        # Create user with defined username and password for login test
        self.user_password = 'password123'
        self.user = User.objects.create_user(username='testuser', password=self.user_password)
        
        # 2. Setup Base Data
        self.author1 = Author.objects.create(name='J.K. Rowling')
        self.author2 = Author.objects.create(name='George Orwell')
        # Book 1: Oldest
        self.book1 = Book.objects.create(title='A Tale of Two Cities', 
                                         publication_year=1859, 
                                         author=self.author1)
        # Book 2: Middle
        self.book2 = Book.objects.create(title='The Great Gatsby', 
                                         publication_year=1925, 
                                         author=self.author2)
        # Book 3: Newest
        self.book3 = Book.objects.create(title='Newest Title', 
                                         publication_year=2020, 
                                         author=self.author1)
        
        # 3. Define URLs 
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book2.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book2.pk})
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        
        # 4. Sample Payloads
        self.valid_payload = {
            'title': 'Test New Book',
            'publication_year': date.today().year,
            'author': self.author2.id 
        }
        self.invalid_payload_future = {
            'title': 'Future Book',
            'publication_year': date.today().year + 1,
            'author': self.author1.id
        }
        self.update_payload = {
            'title': 'Gatsby Updated',
            'publication_year': 1926,
            'author': self.author2.id 
        }

# --------------------------------------------------------------------------------------
#                             A. PERMISSIONS & CRUD TESTS
# --------------------------------------------------------------------------------------

    def test_read_endpoints_unauthenticated(self):
        """Test unauthenticated user can access list and detail views (Read-Only)."""
        list_response = self.client.get(self.list_url)
        detail_response = self.client.get(self.detail_url)
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)

    def test_book_create_authenticated(self):
        """Test authenticated user can create a book using login (201)."""
        # 📢 Using self.client.login() as requested
        self.client.login(username=self.user.username, password=self.user_password)
        response = self.client.post(self.create_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_endpoint_unauthenticated_forbidden(self):
        """Test unauthenticated user cannot create a book (401)."""
        response = self.client.post(self.create_url, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 3)

    def test_book_update_authenticated(self):
        """Test authenticated user can update a book using login (200)."""
        # 📢 Using self.client.login() as requested
        self.client.login(username=self.user.username, password=self.user_password)
        response = self.client.put(self.update_url, self.update_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.title, 'Gatsby Updated')

    def test_book_delete_authenticated(self):
        """Test authenticated user can delete a book using login (204)."""
        # 📢 Using self.client.login() as requested
        self.client.login(username=self.user.username, password=self.user_password)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)
        
    def test_book_delete_unauthenticated_forbidden(self):
        """Test unauthenticated user cannot delete a book (401)."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 3)


# --------------------------------------------------------------------------------------
#                                B. VALIDATION TEST
# --------------------------------------------------------------------------------------

    def test_publication_year_validation_fails(self):
        """Test custom validation prevents creating a book with a future year (400)."""
        self.client.login(username=self.user.username, password=self.user_password)
        response = self.client.post(self.create_url, self.invalid_payload_future, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)


# --------------------------------------------------------------------------------------
#                          C. FILTERING, SEARCHING, ORDERING TESTS
# --------------------------------------------------------------------------------------
    # Note: These tests do not require authentication as they are read-only views.

    def test_book_filter_by_year(self):
        """Test filtering by publication_year."""
        response = self.client.get(f'{self.list_url}?publication_year=1925')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Great Gatsby')
        
    def test_book_search_by_title_or_author(self):
        """Test searching across title and author name."""
        response = self.client.get(f'{self.list_url}?search=Rowling')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
    def test_book_ordering_descending(self):
        """Test ordering by publication year in descending order."""
        # Order by newest first: 2020, 1925, 1859
        response = self.client.get(f'{self.list_url}?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)
        self.assertEqual(response.data[-1]['publication_year'], 1859)
