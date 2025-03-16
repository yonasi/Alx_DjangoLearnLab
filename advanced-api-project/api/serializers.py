from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Task 0
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        
        if value > current_year:
            raise serializers.ValidationError("publication year can not be in the future") # checks the value of publication_year against
                                                                                           # current year if the conditions are right it returns the value(publication_year)
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books'] # because we nest BookSerializer inside Author serializer related book 
                                   # instances are listed with the author. This is achieved by the related_name attribute in author field of Book model
# End task 0