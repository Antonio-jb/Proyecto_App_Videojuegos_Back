from rest_framework import serializers
from videogames.models import Videogame, Genre


class GetVideogameSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='genre.name', allow_null=True)

    class Meta:
        model = Videogame
        fields = ['id', 'title', 'description', 'genre', 'gameImg', 'score', 'slug', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get("title"):
            raise serializers.ValidationError({"error": "El titulo es obligatorio"})
        return data

class GetGenreSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='genre.name', allow_null=True)

    class Meta:
        model = Genre
        fields = '__all__'

    def validate(self, data):
        if not data.get("name"):
            raise serializers.ValidationError({"error": "El nombre es obligatorio"})
        return data