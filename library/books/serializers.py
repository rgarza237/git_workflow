from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ['id', 'name', 'last_name']

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
	# author = AuthorSerializer()
	authors = serializers.StringRelatedField(many=True, read_only=True)
	genres = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = Book
		fields = ['id', 'name', 'publish_year', 'pages', 'price', 'created_at', 'updated_at', 'authors', 'genres']

class BooksAuthorsSerializer(serializers.ModelSerializer):
	class Meta:
		model = BooksAuthors
		fields = ['id', 'book', 'author']

class BooksGenresSerializer(serializers.ModelSerializer):
	class Meta:
		model = BooksGenres
		fields = ['id', 'book', 'genre']