# Create a Book

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)


# >>> book
# <Book: 1984>  # Or similar representation

# Or more explicitly:
# >>> book.title
# '1984'
# >>> book.author
# 'George Orwell'
# >>> book.publication_year
# 1949