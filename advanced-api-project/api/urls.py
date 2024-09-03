from django.urls import path
from .views import ListView
from .views import DetalView
from .views import CreateView
from .views import DeleteView
from .views import UpdateView

## configures the urls for the views.
urlpatterns = [
    path('books/', ListView.as_view(), name = 'book_list'),
    path('books/<int:pk>/', DetalView.as_view(), name = 'book_detail'),
    path('books/add/', CreateView.as_view(), name = 'book_create'),
    path('book/<int:pk>/delete', DeleteView.as_view(), name = 'book_delete'),
    path('books/<int:pk>/edit', UpdateView.as_view(), name = 'book_update' ),
]