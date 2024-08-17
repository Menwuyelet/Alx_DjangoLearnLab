from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

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
    




# Registration View
class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'templates/register.html'
    success_url = reverse_lazy('login')

# Login View
class LoginView(LoginView):
    template_name = 'templates/login.html'

# Logout View
class LogoutView(LogoutView):
    template_name = 'templates/logout.html'
