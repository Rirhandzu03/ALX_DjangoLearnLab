from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render

class BookList(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

  
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on the Book model.
    
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

