from django.urls import path
from .views import BookList

# create your urls here

urlpatterns = [

    path('books/', BookList.as_view(), name='book-list'), # Maps to the BookList view
    
]
