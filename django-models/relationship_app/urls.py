from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('LibraryDetailView/', LibraryDetailView.as_view(), name='LibraryDetailView'),
]
