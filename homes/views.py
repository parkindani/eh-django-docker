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


class HomeList(generics.ListAPIView):
    @api_view(['GET'])
    def get_home_with_name(self):
        queryset = Home.objects.all()
        name = self.query_params.get('name')
        if name:
            print('asdf', name)
            print(queryset)
            queryset = queryset.filter(home_name__contains=name)
            print('exits>>>>>>>>>>>>>>>>>>>')
            print(queryset)
            data = HomeSerializer(queryset).data
            print(data)
            return Response(data, status=status.HTTP_200_OK)
