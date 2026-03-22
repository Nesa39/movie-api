from rest_framework import serializers
from .models import Movie, Director, Actor, Genre, Rating


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id', 'score', 'review', 'user']


class MovieSerializer(serializers.ModelSerializer):

    director = DirectorSerializer(read_only=True)

    actors = ActorSerializer(many=True, read_only=True)

    genres = GenreSerializer(many=True, read_only=True)

    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'