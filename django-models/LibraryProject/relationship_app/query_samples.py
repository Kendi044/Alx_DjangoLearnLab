# django-models/relationship_app/query_samples.py
from .models import Author, Book, Library, Librarian

# Create sample data first
author_name = "J.K. Rowling"
author = Author.objects.create(name=author_name)
book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author, publication_year=1997)
book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author, publication_year=1998)
library_name = "Central Library"
library = Library.objects.create(name=library_name)
library.books.add(book1, book2)
librarian = Librarian.objects.create(name="Jane Doe", library=library)

print("--- Query 1: All books by a specific author ---")
author_object = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(f"Book: {book.title}")

print("\n--- Query 2: All books in a library ---")
library_object = Library.objects.get(name=library_name)
library_books = library_object.books.all()
for book in library_books:
    print(f"Book: {book.title}")

print("\n--- Query 3: Librarian for a library ---")
library_librarian = Library.objects.get(library=library)
print(f"Librarian: {library_librarian.name}")
