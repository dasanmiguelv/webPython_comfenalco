from django.db import models

# Create your models here.

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    type_dish = models.CharField(max_length=200)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name