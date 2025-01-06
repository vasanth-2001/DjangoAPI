from rest_framework import serializers
from .models import BookApi

class BookSerializer(serializers.ModelSerializer):
    author_id=serializers.IntegerField(write_only=True)# for passing request parameter
    class Meta:
        model=BookApi
        fields=['id','title','rating','author_id'] 
        read_only_field=['id'] 