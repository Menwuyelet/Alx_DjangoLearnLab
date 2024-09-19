from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, FollowUserView, UnfollowUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user' ),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user')
]