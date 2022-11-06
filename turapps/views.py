import django_filters
from rest_framework.response import Response
from .models import pereval_added, Coords, Users, Level, Images
from .serializers import PerevalAddedSerializer, CoordsSerializer, LevelSerializer, UsersSerializer, ImagesSerializer
from rest_framework import viewsets

# Create your views here.

class PerevalAddedViewSet(viewsets.ModelViewSet):
    queryset = pereval_added.objects.all()
    serializer_class = PerevalAddedSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["connect","beautyTitle","user_id__email"]

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        instance = self.get_object()
        # проверим пытаются ли изменить информацию о пользователе:
        print(instance.user_id)
        ins_user = Users.objects.filter(pk=instance.user_id)[0]
        # print(ins_user[0].email)
        ses_user = request.data.get('user')
        if ses_user['email'] != ins_user.email \
                or ses_user['fam'] != ins_user.fam or ses_user['name'] != ins_user.name \
                or ses_user['otc'] != ins_user.otc or ses_user['phone'] != ins_user.phone:
            return Response({"state:": 2, "message": "Личные данные изменять нельзя !!!"})
        if not pk or instance.status != "Добавлено":
            return Response({"state:": 0, "message": "Информация на проверке. Изменение не доступно"})

        try:
            instance = pereval_added.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = PerevalAddedSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"state:": 1, "message": "Изменения успешно применены"})


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



