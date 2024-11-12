from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to show in the list view
    list_filter = ('publication_year',)  # Filter by publication year
    search_fields = ('title', 'author')  # Enable search by title and author



