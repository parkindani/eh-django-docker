from django.contrib.auth.models import User, Group
from .models import Home
from decimal import Decimal
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from homes.serializers import UserSerializer, GroupSerializer, HomeSerializer, HomeAllSerializer


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

        if name:
            qs = qs.filter(home_name__contains=name)

        return qs


class HomeAllViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all().exclude(geo_lat_decimal=Decimal('0.000000'))
    pagination_class = None
    serializer_class = HomeAllSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        qs = super().get_queryset()
        nw_lat = self.request.query_params.get('nw_lat', '')
        nw_lng = self.request.query_params.get('nw_lng', '')
        se_lat = self.request.query_params.get('se_lat', '')
        se_lng = self.request.query_params.get('se_lng', '')

        if nw_lat and nw_lng and se_lat and se_lng:
            qs = qs.filter(geo_lat_decimal__gte=Decimal(se_lat))\
                .filter(geo_lat_decimal__lte=Decimal(nw_lat)) \
                .filter(geo_lng_decimal__gte=Decimal(nw_lng)) \
                .filter(geo_lng_decimal__lte=Decimal(se_lng))

        return qs
