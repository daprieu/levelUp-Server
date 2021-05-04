from django.db.models.deletion import SET_NULL
from .gameType import GameType
from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    game_type = models.ForeignKey(GameType, on_delete=SET_NULL, null=True)