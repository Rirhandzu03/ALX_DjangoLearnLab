from relationship_app.models import Author, Book, Library, Librarian

#1. Query all books by a specific author
def books_by_author(author_name):
    try:
        # Retrieve the author object
        author = Author.objects.get(name=author_name)
        # Retrieve all books by the author
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")

    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}.")

#2. List all books in a specific library
def books_in_library(library_name):
    try:
        # Retrieve the library object
        library = Library.objects.get(name=library_name)
        # Retrieve all books in the library
        books = library.books.all()
        print(f"Books in the library '{library_name}':")
        for book in books:
            print(f"- {book.title}")

    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

#3. Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    try:
        # Retrieve the library objects
        library = Library.objects.get(name=library_name)
        # Retrieve the librarian for the library
        librarian = Librarian.objects.get(library=library)
        print(f"The librarian for the library '{library_name}' is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for the library '{library_name}'.")

 
