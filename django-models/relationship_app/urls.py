from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from views import register
from .views import LogoutView
from .views import LoginView
from .views import admin_view
from .views import librarian_view
from .views import member_view


urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('LibraryDetailView/', LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('Admin/', Admin, name='Admin'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]



