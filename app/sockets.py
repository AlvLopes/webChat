import socketio
from fastapi import FastAPI

sio = socketio.AsyncServer(async_mode='asgi'
