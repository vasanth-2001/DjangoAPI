from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import ChefApi
from .serializers import ChefSerializers
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action

# Create your views here.
class ChefViewSet(ModelViewSet):
    queryset = ChefApi.objects.all()
    serializer_class = ChefSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]