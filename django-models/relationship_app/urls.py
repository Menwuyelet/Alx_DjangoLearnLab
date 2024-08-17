from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('LibraryDetailView/', views.AboutView.as_view(), name='about'),
]
