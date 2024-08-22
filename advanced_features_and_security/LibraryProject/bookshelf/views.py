from django.shortcuts import render

# Create your views here.
from django.shortcuts import  get_object_or_404
from django.shortcuts import  redirect
from django.contrib.auth.decorators import permission_required
from bookshelf.models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle book deletion
        book.delete()
        return redirect('book_list')  # Replace with your actual redirect
    return render(request, 'delete_book.html', {'book': book})