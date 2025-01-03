from rest_framework import serializers
from .models import RestApi

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=RestApi
        fields="__all__" #['id','first_name','age']
        read_only_field=['id'] 