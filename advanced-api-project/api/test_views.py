from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.author1 = Author.objects.create(name="testAuthor1")
        self.author2 = Author.objects.create(name="testAuthor2")
        self.book1 = Book.objects.create(title="testBook1", author=self.author1, publication_year="2023-01-01")
        self.book2 = Book.objects.create(title="testBook2", author=self.author2, publication_year="2023-02-02")

    def test_book_list(self):
        url = reverse("book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], "testBook1")

    def test_book_detail(self):
        url = reverse("book_detail", args=[self.book1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "testBook1")

    def test_book_create(self):
        url = reverse("book_list")
        data = {"title": "newBook", "author": self.author1.id, "publication_year": "2023-03-03"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title="newBook").author.name, "testAuthor1")

    def test_book_update(self):
        url = reverse("book_detail", args=[self.book1.pk])
        data = {"title": "updatedBook", "author": self.author2.id, "publication_year": "2023-04-04"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book1.pk).title, "updatedBook")

    def test_book_delete(self):
        url = reverse("book_detail", args=[self.book1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_book_filter_by_author(self):
        url = reverse("book_list") + f"?author={self.author1.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author']['id'], self.author1.id)

    def test_book_search_by_title(self):
        url = reverse("book_list") + "?search=Book2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "testBook2")

    def test_book_ordering_by_publication_year(self):
        url = reverse("book_list") + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "testBook1")

        url = reverse("book_list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "testBook2")

    def test_unauthenticated_access(self):
        self.client.credentials() 
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_post(self):
        self.client.credentials()
        url = reverse('book_list')
        data = {'title': 'New Book', 'author': self.author1.id, 'publication_year': '2023-03-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#Testing Documentation:
#Testing Strategy:
#Unit Tests: functions in isolation from the database
#CRUD Operations: test create, read, update, and delete operations for the Book model.
#Filtering, Searching, and Ordering: Verify that these functionalities work as expected by providing various test cases.
#Authentication and Permissions: Test that only authenticated users with the correct permissions can access and modify the API.