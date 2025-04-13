from rest_framework import serializers
from reviews.models import Review
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from datetime import datetime, time
from django.contrib.auth import get_user_model

from users.serializers.UserSerializer import GetUserSerializer

User = get_user_model()

class AddNewReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError({"message": "Title is required"})
        if not data.get('genre'):
            raise serializers.ValidationError({"message": "Genre is required - RPG = 1 / Terror = 2 / Fantasia = 3"})
        if not data.get('description'):
            raise serializers.ValidationError({"message": "Description is required"})

        return data

class UpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError({"message": "Title is required"})

        return data

class ReviewDateFilterSerializer(serializers.Serializer):
    date = serializers.CharField()

    def validate_date(self, value):
        try:
            parsed_date = datetime.strptime(value, '%Y-%m-%d').date()
            return parsed_date
        except ValueError:
            raise serializers.ValidationError("Formato inválido. Use 'YYYY-MM-DD'.")

class ReviewGenreFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['genre']
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def validate(self,data):
        if not data.get('genre'):
            raise serializers.ValidationError({"message": "Genre is required"})

        return data

class ReviewTitleFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title']
        read_only_fields = ['slug', 'created_at', 'updated_at']


    def validate(self,data):

        if not data.get('title'):
                raise serializers.ValidationError({"message": "title is required"})

        return data

class GetReviewSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='genre.name', allow_null=True)

    class Meta:
        model = Review
        fields = ['id', 'title', 'description', 'date', 'user', 'genre', 'slug', 'stars', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get("title"):
            raise serializers.ValidationError({"error": "El titulo es obligatorio"})
        return data