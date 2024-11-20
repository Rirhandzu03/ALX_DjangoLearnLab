from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

  