# TASK 3.18 - PYTHON REVIEW
# -------------------------
# -------------------------
# -------------------------
# -------------------------

class BookNotFoundException(Exception):
    pass

class BookNotAvailableException(Exception):
    pass

class Book:
    title: str
    author: str
    status: bool

    def __init__(self, title: str, author: str, status: bool = True):
        self.title = title
        self.author = author
        self.status = status

    def isAvailable(self) -> str:
        return "Yes" if self.status else "No"

    def __str__(self):
        return f"Title: {self.title} --- Author: {self.author} --- Available: {self.isAvailable()}"

class Library:
    def __init__(self):
        self.collection = []

    def addBook(self, book: Book):
        self.collection.append(book)

    def getAvailableBooks(self) -> str:
        available_books = [book for book in self.collection if book.status]
        if available_books:
            return "Available Books:\n" + "\n".join(str(book) for book in available_books)
        return "No available books."

    def getBorrowedBooks(self) -> str:
        borrowed_books = [book for book in self.collection if not book.status]
        if borrowed_books:
            return "Borrowed Books:\n" + "\n".join(str(book) for book in borrowed_books)
        return "No borrowed books."

    def borrowABook(self, title: str):
        try:
            book_found = next((book for book in self.collection if book.title == title), None)

            if not book_found:
                raise BookNotFoundException(f"The book with title \"{title}\" could not be found")

            if not book_found.status:
                raise BookNotAvailableException(f"The book with title \"{title}\" is already borrowed")

            book_found.status = False

        except BookNotFoundException as e:
            print(f"{e}")
        except BookNotAvailableException as e:
            print(f"{e}")

    def returnABook(self, title: str):
        try:
            book_found = next((book for book in self.collection if book.title == title), None)

            if not book_found:
                raise BookNotFoundException(f"The book with title \"{title}\" could not be found")

            if book_found.status:
                print(f"The book \"{title}\" is not borrowed.")
                return

            book_found.status = True

        except BookNotFoundException as e:
            print(f"{e}")

    def __str__(self) -> str:
        return "Library Books:\n" + "\n".join(str(book) for book in self.collection)


b1 = Book("Hábitos Atómicos", "James Clear")
b2 = Book("Las 48 leyes del poder", "Robert Greene", False)
b3 = Book("Deja de ser tú", "Joe Dispenza")
b4 = Book("Tus tres superpoderes", "Mario Alonso Puig")
b5 = Book("El ego es el enemigo", "Ryan Holiday", False)

library = Library()
library.addBook(b1)
library.addBook(b2)
library.addBook(b3)
library.addBook(b4)
library.addBook(b5)

print(library)
print()
print(library.getAvailableBooks())
print()
print(library.getBorrowedBooks())

print("\n---- AFTER BORROWING BOOK 'Hábitos Atómicos' ----")
library.borrowABook("Hábitos Atómicos")
print(library.getBorrowedBooks())

print("\n---- AFTER TRYING TO BORROW A BOOK THAT DOESN'T EXIST ----")
library.borrowABook("12 reglas para vivir")

print("\n---- AFTER TRYING TO BORROW A BOOK THAT IS ALREADY BORROWED ----")
library.borrowABook("Las 48 leyes del poder")

print("\n---- AFTER RETURNING BOOK 'Las 48 leyes del poder' ----")
library.returnABook("Las 48 leyes del poder")
print(library.getBorrowedBooks())