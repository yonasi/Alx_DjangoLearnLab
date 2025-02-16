# Retrieve a Book

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Display all attributes
print(book.title)
print(book.author)
print(book.publication_year)

# Output (in the shell):
# 1984
# George Orwell
# 1949