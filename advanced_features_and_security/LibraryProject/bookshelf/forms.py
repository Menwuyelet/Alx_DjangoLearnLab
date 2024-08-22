from django import forms
from .models import Book  # Import necessary model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Replace with your actual model
        fields = ['title', 'author', 'publication_year'] 