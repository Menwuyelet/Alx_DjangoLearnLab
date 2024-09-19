from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
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
        queryset = Post.objects.filter(author__in=following_users)  
        return queryset.order_by('-created_at') 