from rest_framework import serializers

from main.models import *


class MetroStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetroStation
        fields = ('id','name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title')

class ThingReadSerialaizer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    metro = MetroStationSerializer(read_only=True)

    class Meta:
        model = Thing
        fields = ('id','category', 'metro', 'address', 'description', 'thing_photo', 'additional_photo','place_photo', 'created')

class ThingCreateSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = ('category', 'metro', 'address', 'description', 'thing_photo', 'additional_photo','place_photo')

