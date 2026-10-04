from django.db.models.deletion import ProtectedError
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.select_related('breed').all()
    serializer_class = DogSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options']


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError:
            return Response({'detail': 'Delete or reassign dogs using this breed first.'}, status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_204_NO_CONTENT)
