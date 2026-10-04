from rest_framework.routers import SimpleRouter
from .controllers import DogViewSet, BreedViewSet


class OptionalSlashRouter(SimpleRouter):
    """Accept either spelling without redirecting POST/PUT requests."""
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'


router = OptionalSlashRouter()
router.register('dogs', DogViewSet, basename='dog')
router.register('breeds', BreedViewSet, basename='breed')
urlpatterns = router.urls
