from rest_framework import serializers
import datetime
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book ## this assignes the model Book to be serialized
        fields = '__all__' ## tells the fields to serialize whic is all.

    def validate(self, data): ## this validates if the date of publication is not in the feature.
        curent_date = datetime.date.today().year ## assignes the curent date.
        if data > curent_date: ## checks if the publication year is after the current date. 
            raise serializers.ValidationError("Publication year can`t be in the feature.") ## it raises error if the publication date is after the current date.
        return data


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) ## this nestes the Book serializer in side of the author serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books'] ## lists the fields to be serialized including the book_title.