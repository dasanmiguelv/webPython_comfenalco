from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=500)
    age = models.PositiveIntegerField()

    def __str__(self):
        return "{} - {}".format(self.name, self.age)


class Game(models.Model):
    fecha = models.DateTimeField('date published')
    locacion = models.CharField(max_length=500)

    def __str__(self):
        return "{} - {}".format(self.fecha, self.locacion)


class GamePlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    point = models.PositiveIntegerField()
    foul = models.PositiveIntegerField()

    def __str__(self):
        return "{} -  {} - {} -  {}".format(self.player.name, self.game.fecha, self.point, self.foul)

