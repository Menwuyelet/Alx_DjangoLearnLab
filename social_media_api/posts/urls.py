from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, UserFeedView

router = DefaultRouter()
router.register(r'posts', PostView)
router.register(r'comments', CommentView)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user_feed'),
]