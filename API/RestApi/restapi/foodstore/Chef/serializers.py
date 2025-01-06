from rest_framework import serializers
from .models import ChefApi

class ChefSerializers(serializers.ModelSerializer):
    class Meta:
        model=ChefApi
        fields="__all__"
        read_only_field=['id']