from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] ## grants any other user who is not authenticated read only permission

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] ## grants any other user who is not authenticated read only permission

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] ## grants access to authenticated user only.

    def perform_create(self, serializer): ## checks if the title of the book is in use and if it is it raises error.
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title = title).exists():
            raise ValidationError('This title is already in use.')
        serializer.save()

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] ## grants access to authenticated user only.

    def perform_update(self, serializer): ## it checks if the title of the book being updated is empty is it is it raises error.
       title = serializer.validated_data.get('title')
       if not title:
           raise ValidationError('Title can not be empty.')
       serializer.save()

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] ## grants access to authenticated user only.


