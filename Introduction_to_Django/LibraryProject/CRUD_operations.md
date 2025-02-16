# Create a Book

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output (in the shell):
# >>> book
# <Book: 1984>  # Or similar representation

# Or if you want to be more explicit:
# >>> book.title
# '1984'
# >>> book.author
# 'George Orwell'
# >>> book.publication_year
# 1949


# Retrieve a Book

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984") # Assuming title is unique, otherwise use filter and get the first item.

# Display all attributes
print(book.title)
print(book.author)
print(book.publication_year)

# Output (in the shell):
# 1984
# George Orwell
# 1949

# Update a Book

```python
from bookshelf.models import Book

# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()  # Important: Save the changes

# Output (in the shell - you'll see the change after retrieving again):
# >>> book.title
# 'Nineteen Eighty-Four'

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