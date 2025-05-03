#  Class Methods

class Book:
    # Class variable to track the total number of books
    total_books = 0

    # Constructor method to initialize the Book object
    def __init__(self):

        # Every time a new book is created, we increment the book count
        Book.increment_book_count()

    # Class method to increment the total_books count
    @classmethod
    def increment_book_count(cls):
        # Incrementing the total_books class variable
        cls.total_books += 1

# Creating three instances of the Book class
book1 = Book()
book2 = Book()
book3 = Book()

# Printing the total number of books created
print(f"Total Books are: {Book.total_books}")




