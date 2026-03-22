from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Movie, Director, Actor, Genre, Rating
from .serializers import (
    MovieSerializer,
    DirectorSerializer,
    ActorSerializer,
    GenreSerializer
)
from .filters import MovieFilter


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all().order_by('-created_at')
    serializer_class = MovieSerializer

    # ✅ Enable filtering + search
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = MovieFilter
    search_fields = ['title']

    # 🔐 Rate movie (Protected API)
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated]
    )
    def rate(self, request, pk=None):

        movie = self.get_object()

        score = request.data.get("score")
        review = request.data.get("review", "")

        # ❌ Check if score missing
        if score is None:
            return Response(
                {"error": "Score is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ❌ Convert score to integer
        try:
            score = int(score)
        except ValueError:
            return Response(
                {"error": "Score must be a number"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ❌ Validate range
        if score < 1 or score > 5:
            return Response(
                {"error": "Score must be between 1 and 5"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ✅ Create or update rating (one per user)
        Rating.objects.update_or_create(
            movie=movie,
            user=request.user,
            defaults={
                "score": score,
                "review": review
            }
        )

        return Response(
            {"message": "Rating added successfully"},
            status=status.HTTP_201_CREATED
        )


# 🎬 Director View
class DirectorViewSet(viewsets.ModelViewSet):

    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


# 🎭 Actor View
class ActorViewSet(viewsets.ModelViewSet):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


# 🎞 Genre View
class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer