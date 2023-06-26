
print("starty mc start start")
import os
#import json
import time
import datetime

import pika
import sys
from multiprocessing import Process, Manager , freeze_support
import asyncio
import websockets
import json
import sys

import asyncio
import websockets


async def heartbeat(websocket):
    while True:
        try:
            print("time sleep 10")
            await websocket.send(json.dumps({'heartbeat':'heartbeat', 'token': 'hello'}))

            await asyncio.sleep(6)  # Send heartbeat every 60 seconds
            print("time sleep 11 ")
        except websockets.exceptions.ConnectionClosedError:
            print(" heartbeat error ")
            print(9/0)

async def SendSMS():
    ws_url = 'wss://frontend:8000/ws/endpoint/chat/'
    ws_url = 'ws://localhost:8000/ws/endpoint/chat/'
    print(str(ws_url)+ "  ====   url were using ")
    async with websockets.connect(ws_url, ping_interval=None) as websocket:
        asyncio.create_task(heartbeat(websocket))
        i = 0
        while True:
            await asyncio.sleep(0.5)
            i+=1
            if i % 2 == 0:
                msg = "blue"
            else:
                 msg = "red"
            await websocket.send(json.dumps({'from backend':msg, 'token': 'hello'}))

            response = await websocket.recv()


            print("Received response from Django:", response)




def send_SMS_caller():
    asyncio.run(SendSMS())

if __name__ == '__main__':
    freeze_support()
    send_SMS_caller()
