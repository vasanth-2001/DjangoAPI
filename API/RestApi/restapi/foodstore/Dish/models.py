from django.db import models
from Chef.models import ChefApi


# Create your models here.
class DishApi(models.Model):
    Dish_name=models.CharField(max_length=20)
    rating=models.IntegerField()
    chef=models.ForeignKey(ChefApi, on_delete=models.CASCADE)
    