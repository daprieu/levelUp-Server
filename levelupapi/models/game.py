from levelupapi.models.gamer import Gamer
from django.db.models.deletion import SET_NULL
from .gameType import GameType
from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    number_of_players = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=50)
    gamer = models.ForeignKey(Gamer, on_delete=SET_NULL, null=True)
    game_type = models.ForeignKey(GameType, on_delete=SET_NULL, null=True)

    # @property
    # def event_count(self):
    #     return self.__event_count

    # @event_count.setter
    # def event_count(self, value):
    #     self.__event_count = value