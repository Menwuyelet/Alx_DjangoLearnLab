from rest_framework import serializers
from accounts.models import CustomUser
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(queryset=CustomUser.objects.all())
    comments = serializers.StringRelatedField(many=True, queryset=Comment.objects.all(), required=False, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError({'title': 'Title is required'})
        return data

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(queryset=CustomUser.objects.all())
    post = serializers.StringRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        if not data.get('content'):
             raise serializers.ValidationError({'content': 'Content is required'})
        return data
































