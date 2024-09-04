from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User



class BookAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_book(self):
        url = reverse('book_create')  
        data = {
            "title": "Test Book",
            "author": "Test Author",
            "publication_year": 2024
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Test Book")


    def test_update_book(self):
            book = Book.objects.create(title="Old Title", author="Old Author", publication_year=2024)
            url = reverse('book_update', args=[book.id]) 
            data = {
                "title": "New Title",
                "author": "New Author",
                "publication_year": 2023
            }
            response = self.client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            book.refresh_from_db()
            self.assertEqual(book.title, "New Title")
            self.assertEqual(book.author, "New Author")
            self.assertEqual(book.publication_year, 2023)


    def test_delete_book(self):
            book = Book.objects.create(title="TestBook", author="Author", publication_year=2024)
            url = reverse('book_delete', args=[book.id]) 
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(Book.objects.count(), 0)


    def test_filter_books(self):
            Book.objects.create(title="Harry Potter", author="J.K. Rowling", publication_year=2001)
            Book.objects.create(title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937)
            url = f"{reverse('book_list')}?author=J.K. Rowling"
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]['author'], "J.K. Rowling")

    def test_search_books(self):
            Book.objects.create(title="Harry Potter", author="J.K. Rowling", publication_year=2001)
            Book.objects.create(title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937)
            url = f"{reverse('book_list')}?search=Hobbit"
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]['title'], "The Hobbit")

    def test_order_books(self):
            Book.objects.create(title="Harry Potter", author="J.K. Rowling", publication_year=2001)
            Book.objects.create(title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937)
            url = f"{reverse('book_list')}?ordering=publication_year"
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data[0]['title'], "The Hobbit") 

    def test_permissions(self):
            url = reverse('book_list')
            data = {
                "title": "Test Book",
                "author": "Author",
                "publication_year": 2024
            }
            self.client.logout()  
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)