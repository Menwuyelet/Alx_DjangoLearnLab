#python script
retrieved_book = Book.objects.get(title = "1984")
retrieved_book.title = 'Nineteen Eighty-Four'
print(retrieved_book.title) # Nineteen Eighty-Four
