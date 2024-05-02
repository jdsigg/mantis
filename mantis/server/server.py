from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.on('greet')
async def greet(sid):
    print(f"Thank you for the greeting, {sid}")
    await sio.emit('welcome', {'response': f"Welcome to the server, {sid}"})

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    web.run_app(app)