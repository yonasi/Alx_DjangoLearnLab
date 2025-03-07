from django.db import models

# Task 0

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title