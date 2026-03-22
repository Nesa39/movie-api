import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):

    genre = django_filters.CharFilter(
        field_name="genres__name",
        lookup_expr='icontains'
    )

    director = django_filters.CharFilter(
        field_name="director__name",
        lookup_expr='icontains'
    )

    class Meta:
        model = Movie
        fields = ['genre', 'director']