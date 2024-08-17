from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name = 'Jhon Doe')

books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)


library = Library.objects.get(name = library_name)

books_in_library = library.books.all()

for book in books_in_library:
    print(book.title)

librarian_in_a_library = Librarian.objects.filter(library = library)

for librarian in librarian_in_a_library :
    print(library.name)
