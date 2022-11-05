from rest_framework.response import Response
from rest_framework.views import APIView
from .models import pereval_added, Coords, Users, Level, Images
from .serializers import PerevalAddedSerializer, CoordsSerializer, LevelSerializer, UsersSerializer, ImagesSerializer
from rest_framework import viewsets

# Create your views here.

class PerevalAddedViewSet(viewsets.ModelViewSet):
    queryset = pereval_added.objects.all()
    serializer_class = PerevalAddedSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer



class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer



