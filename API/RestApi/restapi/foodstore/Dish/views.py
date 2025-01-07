from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import DishApi
from .serializers import DishSerializers
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
# Create your views here.
class DishViewSet(ModelViewSet):
    queryset = DishApi.objects.all()
    serializer_class = DishSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]