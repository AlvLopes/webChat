from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.sockets import sio_app
from app.routes import router

app = FastAPI(
