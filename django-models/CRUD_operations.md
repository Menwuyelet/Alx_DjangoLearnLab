from bookshelf.models import Book
#creation opration
book = Book.objects.create ( title ='1984', author = 'George Orwell', publication_year = 1949 )
#retrieve opration
retrieved_book = Book.objects.get(title = "1984")
print(retrieved_book.id) # 1
print(retrieved_book.title) # 1984
print(retrieved_book.author) # George Orwell
print(retrieved_book.publication_year) # 1949
#update opration
retrieved_book = Book.objects.get(title = "1984")
retrieved_book.title = 'Nineteen Eighty-Four'
print(retrieved_book.title) # Nineteen Eighty-Four
#delete opration
retrieved_book.delete()
print(Book.object.count()) #0
