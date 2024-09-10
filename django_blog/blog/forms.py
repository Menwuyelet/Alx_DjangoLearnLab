
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User  # Using default User model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # Use the default User model
        fields = ('username', 'email', 'password1', 'password2')