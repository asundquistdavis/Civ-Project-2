import json
from channels.generic.websocket import AsyncWebsocketConsumer
from game.models import Game
from threading import Thread
from _thread import start_new_thread
from asgiref.sync import sync_to_async

class Event(AsyncWebsocketConsumer):
    game = None
    async def connect(self):
        await self.accept()
        self.user = self.scope['user']
        id = self.scope['session']['id']
        self.game = await sync_to_async(Game.objects.filter(id=id)[:1].get)()
        await self.send(text_data=json.dumps({
            'type': 'connection',
            'game': self.game.__str__() if self.game else None,
            'user': self.user.username,
            'status': 'success'
        }))
    
    async def receive(self, text_data=None):
        event = json.loads(text_data)
        type = event['type']
        if type == 'poll':
            id = self.scope['session']['id']
            self.game = await sync_to_async(Game.objects.filter(id=id)[:1].get)()
            await self.send(text_data=json.dumps({
                'type': 'poll',
                'game': self.game.__str__() if self.game else None,
                'user': self.user.username,
                'phase': self.game.phase if self.game else None
            }))

    async def disconnect(self, code):
        pass