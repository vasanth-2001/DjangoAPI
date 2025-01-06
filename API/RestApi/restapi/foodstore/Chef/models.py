from django.db import models

# Create your models here.
class ChefApi(models.Model):
    full_name=models.CharField(max_length=20)
    age=models.IntegerField()
    # image_of_chef=models.ImageField()