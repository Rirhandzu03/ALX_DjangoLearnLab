from rest_framework import serializers
from .models import Author, Book

# BookSerializer - Serializes the Book model and validates publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    
    def validate_publication_year(self, value):
        if value > 2024:  
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer - Serializes the Author model, including a nested list of books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['name', 'books']
