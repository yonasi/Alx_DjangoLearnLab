# Update a Book

```python
from bookshelf.models import Book

# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()  # Save the changes

# Output (in the shell - you'll see the change after retrieving again):
# >>> book.title
# 'Nineteen Eighty-Four'