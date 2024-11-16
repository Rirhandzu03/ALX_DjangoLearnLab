from bookshelf.models import Book

# Create a Book Instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected Output: <Book: 1984 by George Orwell (1949)>

# Retrieve the Created Book
book = Book.objects.get(title="1984")
book  # Expected Output: <Book: 1984 by George Orwell (1949)>

# Update the Book's Title
book.title = "Nineteen Eighty-Four"
book.save()
book  # Expected Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

# Delete the Book Instance
book.delete()
Book.objects.all()  # Expected Output: QuerySet []

