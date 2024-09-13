from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import homeView, registration, profile, post_list, post_detail, Add_post, Update_post, Delete_post

urlpatterns = [
    path('', homeView, name='home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', registration, name="register"),
    path('profile/', profile, name='profile'),
    path('posts/', post_list.as_view(), name='posts'),
    path('posts/<int:pk>/', post_detail.as_view(), name='post_detail'),
    path('posts/new/', Add_post.as_view(), name='new_post'),
    path('posts/<int:pk>/edit/', Update_post.as_view(), name='update_post' ),
    path('posts/<int:pk>/delete/', Delete_post.as_view(), name='delete_post'),
]