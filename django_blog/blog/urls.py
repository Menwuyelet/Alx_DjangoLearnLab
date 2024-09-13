from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import homeView, registration, profile, post_list, post_detail, Add_post, Update_post, Delete_post, list_comment, Add_comment, Update_comment, Delete_comment

urlpatterns = [
    path('', homeView, name='home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', registration, name="register"),
    path('profile/', profile, name='profile'),
    path('posts/', post_list.as_view(), name='posts'),
    path('posts/<int:pk>/', post_detail.as_view(), name='post_detail'),
    path('post/new/', Add_post.as_view(), name='new_post'),
    path('post/<int:pk>/update/', Update_post.as_view(), name='update_post' ),
    path('post/<int:pk>/delete/', Delete_post.as_view(), name='delete_post'),
    path('posts/<int:pk>/comment/',list_comment.as_view(), name='comments' ),
    path('post/<int:pk>/comment/new', Add_comment.as_view(), name='new_comment'),
    path('post/<int:pk>/comment/update', Update_comment.as_view(), name=('edit_comment')),
    path('post/<int:pk>/comment/delete', Delete_comment.as_view(), name=('delete_comment')),
]