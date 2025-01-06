from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import DishApi
from .serializers import DishSerializers
# Create your views here.
class DishViewSet(ModelViewSet):
    queryset = DishApi.objects.all()
    serializer_class = DishSerializers