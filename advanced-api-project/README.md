-The ListView retrievs all books and gives access to both authenticated user and unauthenticated user but it gives readonly permission for unauthenticated users.
-The DetailView retrievs the detail of a book and gives access to both authenticated user and unauthenticated user but it gives readonly permission for unauthenticated users.
-The CreateView creates a book, to do so it validates the title of the book dose not exist else it raises error. it  only gives access to authenticated users.
-The UpdateView edits the existing book and it validats that the title of the book is not empty else it raises error. it only gives access to authenticated users.
-The DeleteView destroys a book. it only gives access to authenticated users.