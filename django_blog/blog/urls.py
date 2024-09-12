from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import homeView, registration, profile

urlpatterns = [
    path('', homeView, name='home page'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', registration, name="register"),
    path('profile/', profile, name='profile'),
]