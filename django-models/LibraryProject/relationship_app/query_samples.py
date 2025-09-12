# django-models/relationship_app/query_samples.py
from .models import Author, Book, Library, Librarian

# Create sample data first
author = Author.objects.create(name="J.K. Rowling")
book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author, publication_year=1997)
book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author, publication_year=1998)
library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)
librarian = Librarian.objects.create(name="Jane Doe", library=library)

print("--- Query 1: All books by a specific author ---")
books_by_author = Book.objects.filter(author__name="J.K. Rowling")
for book in books_by_author:
    print(f"Book: {book.title}")

print("\n--- Query 2: All books in a library ---")
library_books = Library.objects.get(name="Central Library").books.all()
for book in library_books:
    print(f"Book: {book.title}")

print("\n--- Query 3: Librarian for a library ---")
library_librarian = Library.objects.get(name="Central Library").librarian
print(f"Librarian: {library_librarian.name}")