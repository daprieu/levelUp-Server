from django.db import models
from .gamer import Gamer
from .event import Event


class GameEvent (models.Model):

        event = models.ForeignKey(Event, on_delete=models.CASCADE)
        gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)