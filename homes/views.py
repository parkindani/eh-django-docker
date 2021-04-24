from django.contrib.auth.models import User, Group
from .models import Home
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from homes.serializers import UserSerializer, GroupSerializer, HomeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        qs = super().get_queryset()

        name = self.request.query_params.get('name', '')
        geo_lat = self.request.query_params.get('geo_lat', '')
        geo_lng = self.request.query_params.get('geo_lng', '')

        if name:
            qs = qs.filter(home_name__contains=name)

        if geo_lat and geo_lng:
            qs = qs.filter()

        return qs

