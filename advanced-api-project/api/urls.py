from django.urls import path
from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/detail/', BookDetailView.as_view(), name='book-create'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update a book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]
