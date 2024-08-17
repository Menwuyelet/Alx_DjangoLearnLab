from django.urls import path
from . import views

urlpatterns = [
    path('Book_list/', views.book_list, name='book_list'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
]