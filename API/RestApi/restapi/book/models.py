from django.db import models
from author.models import RestApi
# Create your models here.
class BookApi(models.Model):
    title=models.CharField(max_length=20)
    rating=models.IntegerField()
    author=models.ForeignKey(RestApi,on_delete=models.CASCADE)
    