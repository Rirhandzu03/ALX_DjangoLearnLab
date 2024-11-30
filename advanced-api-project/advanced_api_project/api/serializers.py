from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    # Serializes all fields of the Book model and validates publication_year
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        # Ensures the publication year is not in the future
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
     # Serializes the Author model with nested books data
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
