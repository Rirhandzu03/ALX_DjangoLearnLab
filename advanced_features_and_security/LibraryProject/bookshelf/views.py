from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Logic for creating a book (e.g., form processing and saving)
        pass
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle book editing logic (e.g., form processing and saving)
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        # Logic for deleting the book
        book.delete()
        return redirect('book_list')  

    return render(request, 'confirm_delete.html', {'book': book})

# Views to use forms
def search_books(request):
    books = Book.objects.all()  # Default to all books
    if request.method == 'GET' and 'q' in request.GET:
        form = ExampleForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)  # Safe query using ORM
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})