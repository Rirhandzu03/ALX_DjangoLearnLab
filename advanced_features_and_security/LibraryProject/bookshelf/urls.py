from django.urls import path
from . import views

urlpatterns = [
    # Define the URL pattern for the search_books view
    path('search/', views.search_books, name='search_books'),
    # You can add other views here
]
