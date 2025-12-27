from fastapi import FastAPI
import socketio
sio = socketio.AsyncServer(async_mode="asgi")
app = FastAPI()
asgi_app = socketio.ASGIApp(sio, app)
@app.get("/health")
async def health():
    return {"status": "ok"}