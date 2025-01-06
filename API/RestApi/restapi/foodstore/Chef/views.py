from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import ChefApi
from .serializers import ChefSerializers
# Create your views here.
class ChefViewSet(ModelViewSet):
    queryset = ChefApi.objects.all()
    serializer_class = ChefSerializers