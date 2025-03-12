from django.db import models

# Create your models here.

# Task 0
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE) # creates a relationship between the Book and Author models


    def __str__(self):
        return self.title
    
    # End task 0