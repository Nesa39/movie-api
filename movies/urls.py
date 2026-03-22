from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('movies', MovieViewSet)
router.register('directors', DirectorViewSet)
router.register('actors', ActorViewSet)
router.register('genres', GenreViewSet)

urlpatterns = router.urls