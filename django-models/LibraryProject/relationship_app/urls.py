from django.urls import path
from . import views  
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('books/', list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library detail

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'), 

    # Configuration URLS
    path('admin/', views.admin_view, name='admin_view'), 
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/',views.member_view, name='member_view'),
    
    # URLS Patterns for Secured Views
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delte_book'),

]

