from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Task 0

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Tsdlk 2 ViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# task 3 permissions
from rest_framework import permissions
from rest_framework import authentication
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    def list(self, request):
        queryset = Book.objects.all()
        serializer_class = BookSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def create(self, request):
        serializer_class = BookSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_404_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer_class = BookSerializer(book)
            return Response(serializer_class.data)
        
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
             book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer_class = BookSerializer(book, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)