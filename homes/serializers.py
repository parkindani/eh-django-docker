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


class HomeSerializer(serializers.Serializer):
    home_name = serializers.CharField(max_length=500)