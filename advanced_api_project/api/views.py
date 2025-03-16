from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions
from .models import Book, Author
from .serializers import BookSerializer, Authorserilizer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

# Task 1
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    ordering_fields = ['title', 'author', 'publication_date'] # ordering fields
    ordering = ['title'] # default ordering
    search_fields = ['title', 'author'] # search fields
    

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise serializer.ValidationError('only staff users can create books')
        
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise serializer.ValidationError('only staff users can update books')
        
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_destroy(self, serializer):
        if self.request.user.is_staff:
            isinstance.save()
        else:
            raise serializer.ValidationError('only staff users can delete books')
    