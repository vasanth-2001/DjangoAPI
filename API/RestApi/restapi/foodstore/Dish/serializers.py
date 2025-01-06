from rest_framework import serializers
from .models import DishApi

class DishSerializers(serializers.ModelSerializer):
    chef_id=serializers.IntegerField(write_only=True)
    class Meta:
        model=DishApi
        fields=['Dish_name','rating','chef','chef_id']
        read_only_field=['id']