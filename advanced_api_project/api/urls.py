from django.urls import path, include
from .views import (
    BookListView,
    BookDetailView,
    BookCreateview,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('/books/', BookListView.as_view(), name='book_list'),
    path('/books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('/books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('/books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('/books/create/', BookCreateview.as_view(), name='book_create'),
]