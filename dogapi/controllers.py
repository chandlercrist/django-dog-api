from django.shortcuts import get_object_or_404
from django.db.models.deletion import ProtectedError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

class DogList(APIView):
    def get(self, request):
        return Response(DogSerializer(Dog.objects.all(), many=True).data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DogDetail(APIView):
    def get(self, request, pk):
        return Response(DogSerializer(get_object_or_404(Dog, pk=pk)).data)

    def put(self, request, pk):
        serializer = DogSerializer(get_object_or_404(Dog, pk=pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = get_object_or_404(Dog, pk=pk)
        try:
            instance.delete()
        except ProtectedError:
            return Response({'detail': 'Delete or reassign dogs using this breed first.'}, status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(APIView):
    def get(self, request):
        return Response(BreedSerializer(Breed.objects.all(), many=True).data)

    def post(self, request):
        serializer = BreedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BreedDetail(APIView):
    def get(self, request, pk):
        return Response(BreedSerializer(get_object_or_404(Breed, pk=pk)).data)

    def put(self, request, pk):
        serializer = BreedSerializer(get_object_or_404(Breed, pk=pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = get_object_or_404(Breed, pk=pk)
        try:
            instance.delete()
        except ProtectedError:
            return Response({'detail': 'Delete or reassign dogs using this breed first.'}, status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_204_NO_CONTENT)


