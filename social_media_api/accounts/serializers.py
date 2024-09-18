from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


CustomUser = get_user_model()

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
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

## learn and work on your own 

    def validate(self, data):
        user = CustomUser.objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            return user
        raise serializers.ValidationError("Invalid login credentials")