from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


CustomUser = get_user_model().objects.create_user

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'bio', 'profile_picture' ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        token, _ = Token.objects.get_or_create(user=user)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    token = serializers.CharField(read_only=True) 

    class Meta:
        fields = ['email', 'password', 'token']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if user:
            token, _ = Token.objects.create(user=user)
            data['token'] = token.key
            return data
        else:
            raise serializers.ValidationError('Invalid credentials')