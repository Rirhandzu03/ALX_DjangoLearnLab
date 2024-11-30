from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render

# Create your views here.

# ListView for retrieving all books
class BookListView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serailizer_class = BookSerializer

# DetailView for retrieving a single book by ID
class BookDetailView(generics.CreateAPIVew):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CreateView for adding a new book
class BookCreateView(generics.APIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # Automatically assign the authenticated user as the author
        serializer.save(author=self.request.user)  # Assuming the user is an author
        
    def create(self, request, *args, **kwargs):
        """
        Overriding the default 'create' method to include additional validation logic
        before creating the book.
        """
        publication_year = request.data.get('publication_year')

        # Custom validation to check if the publication year is in the future
        if publication_year and int(publication_year) > 2024:  # Example future year check
            return Response(
                {'error': 'Publication year cannot be in the future'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

# UpdateView for modifying an existing book
class BookUpdateView(generics.APIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        """
        Perform the actual update of the book.
        You can add custom logic here to validate changes.
        """
        # Example: Prevent changing the author of a book once it's published
        original_author = self.get_object().author
        new_author = serializer.validated_data.get('author', None)

        if new_author and new_author != original_author:
            raise serializer.ValidationError("You cannot change the author once the book is published.")
        
        # Save the updated instance
        serializer.save()

    def update(self, request, *args, **kwargs):
        """
        Override the default 'update' method to add custom validation logic.
        """
        publication_year = request.data.get('publication_year')

        if publication_year and int(publication_year) > 2024:
            return Response(
                {'error': 'Publication year cannot be in the future'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().update(request, *args, **kwargs)


# DeleteView for removing a book
class BookDeleteView(generics.APIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer





