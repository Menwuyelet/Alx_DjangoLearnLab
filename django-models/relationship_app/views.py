from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required

from .forms import BookForm

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
    




class register(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')


class LoginView(Login):
    template_name = 'templates/login.html'


class LogoutView(Logout):
    template_name = 'templates/logout.html'




def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


def is_librarian(user):
    return user.userprofile.role == 'Librarians'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")



def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")





@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') 
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)  
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list') 
    return render(request, 'delete_book.html', {'book': book})
