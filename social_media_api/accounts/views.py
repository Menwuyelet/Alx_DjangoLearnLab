from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework. response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserLoginSerializer
# Create your views here.


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user).key
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'token': serializer.validated_data['token']}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        return Response({
            'email': user.email,
            'username': user.username,
            'bio': user.bio,
            'profile_picture': user.profile_picture.url if user.profile_picture else None,
            'followers': user.followers.count(),
            'following': user.following.count()
        }, status=status.HTTP_200_OK)