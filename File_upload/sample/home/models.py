from django.db import models


# Create your models here.
class employee(models.Model):
    File = models.FileField(default=True)
    image = models.ImageField(default=True)

    class Meta:
        db_table = "emp"
