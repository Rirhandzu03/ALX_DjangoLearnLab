from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

        # Create test books
        self.book1 = Book.objects.create(title="Book One", author="Author One", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two",publication_year=2021)

        self.list_url = "/api/books/"

    def test_list_books(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """Test creating a new book"""
        data = {
            "title": "Book Three",
            "author": "Author Three",
            "publication_year": 2022
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Book Three")

    def test_update_book(self):
        """Test updating an existing book"""
        update_url = f"/api/books/{self.book1.id}/"
        data = {
            "title": "Updated Book One",
            "author": "Updated Author One",
            "publication_year": 2023
        }
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book(self):
        """Test deleting a book"""
        delete_url = f"/api/books/{self.book1.id}/"
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """Test filtering books by author"""
        filter_url = f"{self.list_url}?author=Author One"
        response = self.client.get(filter_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author One")

    def test_permissions(self):
        """Test that only authenticated users can access the API"""
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)    

