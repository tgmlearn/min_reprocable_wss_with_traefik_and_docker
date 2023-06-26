from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/endpoint/', consumers.ChatConsumer.as_asgi())
    path('ws/endpoint/<str:room_name>/', consumers.ChatConsumer.as_asgi())
]
