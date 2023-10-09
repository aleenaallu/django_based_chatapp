import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Save the message to the database
        sender = "User"  # You can replace this with the actual sender's information
        await self.save_message(sender, message)

        # Send the message to the chat
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def save_message(self, sender, message):
        # Save the message to the database
        Message.objects.create(sender=sender, content=message)
