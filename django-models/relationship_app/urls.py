from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('book_list/', list_books, name='book_list'),
    path('LibraryDetailView/', LibraryDetailView.as_view(), name='about'),
]
