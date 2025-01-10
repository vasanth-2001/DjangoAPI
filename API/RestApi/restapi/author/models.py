from django.db import models

# Create your models here.
class RestApi(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    image=models.ImageField(upload_to='auhtor_image/',null=True,blank=True)
