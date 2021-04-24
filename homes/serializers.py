from django.contrib.auth.models import User, Group
from .models import Home
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class HomeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['home_name', 'geo_lat_decimal', 'geo_lng_decimal']
