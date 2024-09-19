from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Like
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
from rest_framework import status
from notifications.utils import create_notification 
from notifications.serializers import NotificationSerializer
# Create your views here.



class isAuthor(permissions.BasePermission):
    def has_object_permission(self, request, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user



class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')  
    content = filters.CharFilter(lookup_expr='icontains')  

    class Meta:
        model = Post
        fields = ['title', 'content']


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [isAuthor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)



class CommentFilter(filters.FilterSet):
    post = filters.NumberFilter()  
    class Meta:
        model = Comment
        fields = ['post']

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [isAuthor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CommentFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at') 
        permissions.IsAuthenticated
        return queryset
    


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        user = request.user
        post = get_object_or_404(Post, id=post_id)

        # Check if the user has already liked this post
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=user, post=post)

        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                content_type = ContentType.objects.get_for_model(post),
                object_id=post.id
            )

        return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)
    
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        user = request.user
        post = get_object_or_404(Post, id=post_id)


        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"error": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)


        like.delete()

        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="unliked your post",
                content_type=ContentType.objects.get_for_model(post),
                object_id=post.id
            )

        return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
    
class CommentPostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
       
        create_notification(
            recipient=post.author,
            actor=request.user,
            verb='commented on your post',
            target=post
        )
        return Response({"message": "Comment added."}, status=status.HTTP_200_OK)
    
from rest_framework import generics, permissions
from rest_framework.response import Response
from notifications.models import Notification

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')