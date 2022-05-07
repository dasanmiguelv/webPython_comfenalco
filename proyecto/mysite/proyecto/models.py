from django.db import models

# Create your models here.

class Game(models.Model):
    fecha = models.DateTimeField('date published')
    locacion = models.CharField(max_length=500)


    def __str__(self):
        return "{} - {}".format(self.fecha, self.locacion)

class Person(models.Model):
    name = models.CharField(max_length=500)
    age = models.PositiveIntegerField()


    def __str__(self):
        return "{} - {}".format(self.name, self.age)