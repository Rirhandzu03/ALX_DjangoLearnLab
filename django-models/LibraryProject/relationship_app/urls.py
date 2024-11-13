from django.urls import path
from . import views  # Import views from the current app
from .views import LibraryDetailView, list_books  # Explicitly import both views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library detail
]
