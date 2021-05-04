from django.db import models
from .game import Game

class Event(models.Model):

    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
