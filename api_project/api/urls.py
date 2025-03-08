from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookList

#Task 2
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    # Task 2
    path('', include(router.urls)),
]