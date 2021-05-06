from levelupapi.models.gamer import Gamer
from django.db import models
from .game import Game
from django.db.models.deletion import SET_NULL


class Event(models.Model):

    organizer = models.ForeignKey(Gamer, on_delete=SET_NULL, null=True)
    description = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
