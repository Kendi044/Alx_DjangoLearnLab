# api/models.py

from django.db import models

# Model to store Author information.
class Author(models.Model):
    """
    Model representing an Author.
    name: The author's full name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Model to store Book information, linked to an Author.
class Book(models.Model):
    """
    Model representing a Book.
    title: The title of the book.
    publication_year: The year the book was published.
    author: ForeignKey link to Author (one-to-many). 
            related_name='books' allows Author instance to access related books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
