from levelupapi.models.gamer import Gamer
from django.db import models
from .game import Game
from django.db.models.deletion import SET_NULL

class Event(models.Model):

    organizer = models.ForeignKey(Gamer, on_delete=SET_NULL, null=True)
    description = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='events')
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    attendees = models.ManyToManyField("Gamer", through="gameEvent", related_name="attending")
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

    @property
    def attendee_count(self):
        return self.__attendee_count

    @attendee_count.setter
    def attendee_count(self, value):
        self.__attendee_count = value
