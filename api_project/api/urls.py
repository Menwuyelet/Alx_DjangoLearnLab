from django.urls import path
from .views import BookList

urlpattern = [
    path('books/', BookList.as_view(), name='book_list'),
]