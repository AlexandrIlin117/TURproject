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
    user = UsersSerializer(read_only=True)
    coords = CoordsSerializer(read_only=True)
    level = LevelSerializer(read_only=True)
    images = ImagesSerializer(read_only=True, many=True)
    class Meta:
        model = pereval_added
        fields = ('beautyTitle','title','other_titles','connect',
                  'add_time','status','user','coords','level','images')

    # def create(self, validated_data):
    #     return pereval_added.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.date_added = validated_data.get('date_added',instance.date_added)
    #     instance.raw_data = validated_data.get('raw_data',instance.raw_data)
    #     instance.images = validated_data.get('raw_data',instance.raw_data)
    #     instance.status = validated_data.get('status',instance.status)
    #     instance.save()
    #     return instance