from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User  # Using default User model

class UserCreation(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')

class profileUpdate(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')