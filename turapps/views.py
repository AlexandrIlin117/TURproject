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


class PerevalAddedAPIView(APIView):
    def get(self, request):
        p = pereval_added.objects.all()
        return Response({'post':PerevalAddedSerializer(p, many=True).data})

    def post(self,request):
        serializer = PerevalAddedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post':PerevalAddedSerializer.data})

    def put(self,request,*args, **kwargs):
        pk = kwargs.get("pk", None)
        print(pk)
        if not pk:
            return Response({'error':'Method PUTIN not allowed'})

        try:
            instance = pereval_added.get(pk=pk)
        except:
            return Response({'error':'Method PUTOUT not allowed'})

        serializer = PerevalAddedSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post':PerevalAddedSerializer.data})


