from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    author_name = serializers.CharField(source='Author.name')

    class Meta:
        model = Book
        fields = '__all__'
