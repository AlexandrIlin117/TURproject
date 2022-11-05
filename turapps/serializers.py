from .models import *
from rest_framework import serializers
from .models import pereval_added




class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'fam', 'name','otc','phone')


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude','longitude','height')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter','summer','autumn','spring')

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('data','title')


class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)
    class Meta:
        model = pereval_added
        fields = ('beautyTitle','title','other_titles','connect',
                  'add_time','status','user','coords','level','images')

    def create(self, validated_data):
        print(validated_data)
        # Уберем список изображений из словаря validated_data и сохраним его
        images = validated_data.pop('images')
        # Аналогично обрабатываем содержащиеся в JSON составляющие для полей 'user','coords' и 'level';
        # Проверим есть ли уже пользователь с такой почтой. Если есть используем его ID для заполнения поля в таблице
        # перевалы. Если нет то создадим новую запись в таблице пользователей;
        current_user = validated_data.pop('user')
        ses_email = current_user['email']
        ses_fam = current_user['fam']
        ses_name = current_user['name']
        ses_otc = current_user['otc']
        ses_phone = current_user['phone']
        list_user = Users.objects.all()
        check = False
        for next_user in list_user:
            if next_user.email == ses_email:
                user_id = next_user
                check = True
                break
        if not check:
            Users.objects.create(email=ses_email, fam=ses_fam,name=ses_name,otc=ses_otc,phone=ses_phone)
            user_id = Users.objects.filter(email=ses_email)[0]
            print(user_id, type(user_id))
        # Создадим новые записи в таблицах уровня сложности и координат используя данные из запроса. А ID полученных
        # записей используем при создании записи в таблице перевалов;
        # Обработка координат;
        current_coords = validated_data.pop('coords')
        ses_latitude = current_coords['latitude']
        ses_longitude = current_coords['longitude']
        ses_height = current_coords['height']
        Coords.objects.create(latitude=ses_latitude, longitude=ses_longitude, height=ses_height)
        coord_id = Coords.objects.filter(latitude=ses_latitude)[0]
        # Обработка уровня сложности;
        current_level = validated_data.pop('level')
        ses_winter = current_level['winter']
        ses_summer = current_level['summer']
        ses_autumn = current_level['autumn']
        ses_spring = current_level['spring']
        Level.objects.create(winter=ses_winter, summer=ses_summer, autumn=ses_autumn, spring=ses_spring)
        level_id = Level.objects.filter(winter=ses_winter).filter(summer=ses_summer).filter(autumn=ses_autumn).filter(spring=ses_spring)[0]
        # добавляем ID пользователя, координат и сложности в словарь необходимый
        # для создания новой записи в таблице перевал;
        print(validated_data)
        print(coord_id)
        print(level_id)
        print(user_id)
        print('--------------------')
        validated_data.setdefault('user',user_id)
        validated_data.setdefault('coords', coord_id)
        validated_data.setdefault('level', level_id)

        # Создадим новую запись о перевале;
        pereval = pereval_added.objects.create(**validated_data)

        # Для каждого изображения из списка изображений
        for image in images:
            # Создадим новую запись или получим существующий экземпляр из БД
            current_image, status = Images.objects.get_or_create(
                **image)
            # Поместим ссылку на каждое изображение в вспомогательную таблицу
            # Не забыв указать к какому перевалу оно относится
            PerevalImages.objects.create(
                images=current_image, pereval=pereval)
        return pereval
