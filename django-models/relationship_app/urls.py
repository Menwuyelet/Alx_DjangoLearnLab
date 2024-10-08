from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from views import register
from .views import LogoutView
from .views import LoginView
from .views import admin_view
from .views import librarian_view
from .views import member_view
from .views import add_book_view
from .views import edit_book_view
from .views import delete_book_view

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('LibraryDetailView/', LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('admin/', admin_view, name='Admin'),
    path('librarian/', librarian_view, name='Librarian'),
    path('member/', member_view, name='Member'),
    path('add_book//', add_book_view, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book_view, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book_view, name='delete_book'),
]




