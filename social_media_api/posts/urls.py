from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, UserFeedView, LikePostView, UnlikePostView, CommentPostView

router = DefaultRouter()
router.register(r'posts', PostView)
router.register(r'comments', CommentView)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user_feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
    path('posts/<int:post_id>/comment/', CommentPostView.as_view(), name='comment-post')
]