from datetime import datetime
from .main import sio
rooms = {}
@sio.event
async def connect(sid, environ):
    pass
@sio.event
async def disconnect(sid):
    pass
@sio.event
async def join_room(sid, data):
    pass
@sio.event
async def send_message(sid, data):
    pass