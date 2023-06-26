import json
import random
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync



class ChatConsumer(WebsocketConsumer):
    def connect(self):
#        self.most_recent_message_from_html = "none"
#        self.messages_recieved = 0

        print('connected')
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        print(f"Connected to {self.room_group_name}")

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print("Recived ="+str(text_data))

        json_data = json.loads(text_data)

        try:
            message = json_data["message"]
            print("message ... just message")
            print(message)
        except:
            try:
                message = json_data["from_html"]
                print("message from  from_html")
                print(message)
            except:
                try:
                    message = json_data["from backend"]
                    print("message from  from_backend")
                    print(message)
                    
                    async_to_sync(self.channel_layer.group_send)(
                        self.room_group_name, {"type": "chat_message", "message": message}
                    )

                except:
                    message = json_data["heartbeat"]
                    print("message from  from_heartbeat")


            # Send message to room group




        #        self.send_response("Response from Django: " + message)



    def send_response(self, message):
        # Send the response message to the WebSocket
        self.send(json.dumps({'message2': message}))

######

    def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
