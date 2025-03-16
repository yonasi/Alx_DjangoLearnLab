from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.book1 = Book.objects.create(title='Test Book 1', author='Author 1', publication_year='2023-01-01')
        self.book2 = Book.objects.create(title='Test Book 2', author='Author 2', publication_year='2023-02-01')

    def test_book_list(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_book_create(self):
        url = reverse('book_list')
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': '2023-03-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title='New Book').author, 'New Author')

    def test_book_detail(self):
        url = reverse('book_detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book 1')

    def test_book_update(self):
        url = reverse('book_detail', args=[self.book1.id])
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': '2023-04-01', 'isbn': '5544332211'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book1.id).title, 'Updated Book')

    def test_book_delete(self):
        url = reverse('book_detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_book_filter_by_author(self):
        url = reverse('book_list') + '?author=Author 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 1')

    def test_book_search_by_title(self):
        url = reverse('book_list') + '?search=Book 2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 2')

    def test_book_ordering_by_publication_year(self):
        url = reverse('book_list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

        url = reverse('book_list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book 2')

    def test_unauthenticated_access(self):
        self.client.credentials() #Remove credentials
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) #Or 403, depending on your permission settings

    def test_unauthorized_post(self):
        self.client.credentials()
        url = reverse('book_list')
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': '2023-03-01', 'isbn': '1122334455'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) #Or 403 depending on permissions