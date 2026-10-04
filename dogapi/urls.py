from django.urls import re_path
from .controllers import DogList, DogDetail, BreedList, BreedDetail

urlpatterns = [
    re_path(r'^dogs/?$', DogList.as_view(), name='dog-list'),
    re_path(r'^dogs/(?P<pk>[0-9]+)/?$', DogDetail.as_view(), name='dog-detail'),
    re_path(r'^breeds/?$', BreedList.as_view(), name='breed-list'),
    re_path(r'^breeds/(?P<pk>[0-9]+)/?$', BreedDetail.as_view(), name='breed-detail'),
]
