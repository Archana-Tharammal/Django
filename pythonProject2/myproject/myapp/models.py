from django.db import models

# Create your models here.
class product(models.Model):
    pro_name=models.CharField(max_length=20)
    pro_img=models.ImageField()