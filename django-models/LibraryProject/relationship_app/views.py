from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Library, UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User


# Applying permissions

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Logic for adding a book
    pass

@permission_required('relationship_app.change_book', raise_exception=True)
def edit_book(request, book_id):
    # Logic for editing a book
    book = get_object_or_404(Book, id=book_id)
    pass

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def  delete_book(request, book_id):
    # Logic for deleting a book
    book = get_object_or_404(Book, id=book_id)

# Admin view, only accessible by users with the 'Admin' role
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')  # Admin page template

# Librarian view, only accessible by users with the 'Librarian' role
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')  # Librarian page template

# Member view, only accessible by users with the 'Member' role
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')  # Member page template

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form .is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please try again.')

    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form}) 
    

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# Function-based view
def list_books(request):
    books = Book.objects.all()  # Get all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

