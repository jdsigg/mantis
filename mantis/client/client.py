import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')
    await sio.emit('greet')

@sio.event
async def disconnect():
    print('disconnected from server')

@sio.on('welcome')
def welcome(data):
    print(data['response'])

async def main():
    await sio.connect('http://localhost:8080')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())