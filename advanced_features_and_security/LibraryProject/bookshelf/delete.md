# Delete a Book

```python
from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion (try to retrieve all books again)
books = Book.objects.all()
print(books)  # Should return an empty QuerySet

# Output (in the shell):
# >>> <QuerySet []>