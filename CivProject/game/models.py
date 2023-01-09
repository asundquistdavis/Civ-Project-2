from django.db import models
from datetime import datetime
from time import sleep

from asgiref.sync import sync_to_async

class Game(models.Model):
    start_date = models.DateTimeField(default=datetime.now())
    phase = models.CharField(max_length=15, default='start_game')

    def __str__(self) -> str:
        return f'Civ game {self.id} started on {self.start_date}'

    def run(self):
        print('started new game')
        self.clock()
        print('changing phase')
        self.phase = 'movement'
        print('new phase')
        self.save()

    def clock(self):
        sleep(10)