from django.db import models
from django.contrib.auth.models import User

class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    actors = models.ManyToManyField(Actor)

    genres = models.ManyToManyField(Genre)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Rating(models.Model):

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="ratings"
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    score = models.IntegerField()

    review = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)