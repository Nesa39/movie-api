from django.contrib import admin
from .models import Movie, Director, Actor, Genre, Rating

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)